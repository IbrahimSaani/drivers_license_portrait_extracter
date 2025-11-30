import cv2
import numpy as np

def load_image(image_bytes):
    """Convert uploaded image bytes into OpenCV format."""
    image = np.frombuffer(image_bytes, np.uint8)
    return cv2.imdecode(image, cv2.IMREAD_COLOR)

def detect_faces_haar(image, scale_factor=1.1, min_neighbors=5):
    """Detect faces with OpenCV's Haar Cascade."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)
    
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=scale_factor,
        minNeighbors=min_neighbors
    )
    
    boxes = []
    for (x, y, w, h) in faces:
        boxes.append((x, y, x + w, y + h))
    return boxes

def crop_faces(image, boxes, margin=0.1):
    """Crop detected faces with small margin."""
    h, w, _ = image.shape
    cropped = []
    for (x1, y1, x2, y2) in boxes:
        dx = int((x2 - x1) * margin)
        dy = int((y2 - y1) * margin)
        x1m = max(0, x1 - dx)
        y1m = max(0, y1 - dy)
        x2m = min(w, x2 + dx)
        y2m = min(h, y2 + dy)
        cropped.append(image[y1m:y2m, x1m:x2m])
    return cropped

def draw_boxes(image, boxes):
    """Return image with green boxes drawn around faces."""
    output = image.copy()
    for (x1, y1, x2, y2) in boxes:
        cv2.rectangle(output, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return output
