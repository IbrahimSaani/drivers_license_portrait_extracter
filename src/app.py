import streamlit as st
import cv2
from face_extractor.detector import load_image, detect_faces_haar, crop_faces, draw_boxes

st.set_page_config(page_title="Driver's License Portrait Extractor", layout="wide")

st.title("🪪 Driver’s License Portrait Extraction System")
st.write("Upload a driver’s license image to automatically extract the portrait photo using OpenCV Haar Cascade.")

# Upload image
uploaded_file = st.file_uploader("Upload Driver’s License Image", type=["jpg", "jpeg", "png", "webp"])

# Sidebar settings
st.sidebar.header("Extraction Settings")

# Sensitivity slider
sensitivity = st.sidebar.slider(
    "Face Detection Sensitivity (higher = more detection)",
    1, 10, 5
)

crop_margin = st.sidebar.slider("Crop Margin (%)", 0, 50, 10) / 100
return_type = st.sidebar.radio("Return", ["Main Portrait", "All Faces"])
max_faces = st.sidebar.number_input("Max Faces (when returning all)", 1, 10, 3)

# Process image
if uploaded_file is not None:
    bytes_data = uploaded_file.read()
    image = load_image(bytes_data)

    if image is None:
        st.error("Could not read the image. Please try a different file.")
    else:
        st.subheader("Original Uploaded Image")
        st.image(image, channels="BGR")

        # Adjust detection sensitivity
        scale_factor = 1.05 + (10 - sensitivity) * 0.03

        # 🧠 Detect faces using Haar Cascade
        boxes = detect_faces_haar(image, scale_factor=scale_factor, min_neighbors=5)

        if boxes:
            st.success(f"Detected {len(boxes)} face(s).")

            # 🟩 Draw GREEN bounding boxes
            overlay_image = draw_boxes(image, boxes)
            st.subheader("🔍 Detection Overlay")
            st.image(overlay_image, channels="BGR")

            # Crop faces
            cropped_faces = crop_faces(image, boxes, margin=crop_margin)

            if return_type == "Main Portrait":
                largest = max(cropped_faces, key=lambda img: img.shape[0] * img.shape[1])
                st.subheader("🖼 Extracted Portrait")
                st.image(largest, channels="BGR")

                retval, buffer = cv2.imencode(".jpg", largest)
                st.download_button(
                    "📥 Download Portrait",
                    buffer.tobytes(),
                    file_name="drivers_license_portrait.jpg",
                    mime="image/jpeg"
                )

            else:
                st.subheader("All Detected Faces")
                for i, face in enumerate(cropped_faces[:max_faces]):
                    st.image(face, channels="BGR", caption=f"Face {i+1}")

                import io, zipfile
                zip_buffer = io.BytesIO()

                with zipfile.ZipFile(zip_buffer, "a") as zip_file:
                    for i, face in enumerate(cropped_faces[:max_faces]):
                        ok, buf = cv2.imencode(".jpg", face)
                        if ok:
                            zip_file.writestr(f"portrait_{i+1}.jpg", buf.tobytes())

                st.download_button(
                    "📦 Download All as ZIP",
                    zip_buffer.getvalue(),
                    file_name="portraits.zip",
                    mime="application/zip"
                )

        else:
            st.error("⚠ No faces detected. Try a clearer driver's license image.")
