# 🚗 Driver’s License Portrait Extraction System

This is a **Streamlit-based computer vision application** that automatically detects and extracts **portrait photos from driver’s licenses** using **OpenCV Haar Cascade face detection**.

---

## 📸 **Project Overview**

✔ Upload a driver’s license image  
✔ Detect face(s) automatically  
✔ Extract only the **main portrait**  
✔ Preview detection overlay  
✔ Download extracted portrait as `.jpg`

---

## 📁 **Project Structure**

drivers_license_portrait_extractor/
│
├─ .venv/                      # Virtual environment (ignored in git)
│
├─ src/
│   ├─ app.py                  # Streamlit main app (UI)
│   │
│   └─ face_extractor/
│       ├─ __init__.py         # Makes folder importable
│       └─ detector.py         # OpenCV Haar-based face detection
│
├─ requirements.txt            # Dependencies
├─ README.md                   # Project documentation
└─ .gitignore                  # Files to ignore in Git




---

## ⚙️ **Installation & Setup**

### 1️⃣ Create Virtual Environment (Recommended)
```bash
python -m venv .venv


2️⃣ Activate It
🪟 Windows PowerShell

.venv\Scripts\Activate.ps1


3️⃣ Install Dependencies

pip install --upgrade pip
pip install -r requirements.txt


▶️ Run the Application

streamlit run src/app.py


📦 requirements.txt

streamlit
opencv-python-headless
numpy
Pillow

🧠 How It Works (Simplified)

User uploads a driver’s license image

The image is read using OpenCV

Face detection is applied using Haar Cascade

The largest detected face is assumed to be the driver

The face is cropped and displayed

User can download the extracted portrait

🛠️ Tech Stack

| Component      | Technology Used       |
| -------------- | --------------------- |
| UI Framework   | Streamlit             |
| Image Handling | OpenCV + NumPy        |
| Detection      | OpenCV Haar Cascades  |
| Language       | Python                |
| IDE            | VS Code (recommended) |
