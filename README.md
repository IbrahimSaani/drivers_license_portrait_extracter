## Driver’s License Portrait Extraction System

A lightweight Streamlit app to automatically detect and extract the portrait from a driver’s license image.

 ## Overview

This project uses OpenCV Haar-based face detection to automatically locate and crop only the portrait photo from a driver’s license image. It provides a simple web interface built using Streamlit, where users can upload an image and instantly extract the portrait — no training or complex setup required!

## Features

✔ Upload any driver’s license image (.jpg, .jpeg, .png, .webp)
✔ Automatic face detection using OpenCV Haar Cascade
✔ Extract only the largest face (driver’s main portrait)
✔ Adjustable detection sensitivity & crop margin
✔ Download the extracted portrait directly
✔ 100% offline — runs locally
✔ Clean modular code structure

🗂️ Project Structure
drivers_license_portrait_extractor/
│
├─ src/
│   ├─ app.py                # Streamlit interface (main app)
│   └─ face_extractor/
│        ├─ __init__.py     # Makes functions importable
│        └─ detector.py     # Face detection + cropping (OpenCV Haar cascade)
│
├─ requirements.txt         # Dependencies
├─ README.md                # Project documentation
└─ .gitignore               # Ignore unnecessary files

⚙️ Installation & Setup
1️⃣ Create Virtual Environment (Recommended)

Windows PowerShell

python -m venv .venv


macOS / Linux

python3 -m venv .venv

2️⃣ Activate It

Windows PowerShell

.venv\Scripts\Activate.ps1


macOS / Linux

source .venv/bin/activate

3️⃣ Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt

▶️ Run the App
streamlit run src/app.py


Once the browser opens:

Upload a driver’s license image

Adjust detection sensitivity & crop margin

Get your portrait automatically!

🧠 How It Works (Simple Explanation)

You upload a driver’s license image

OpenCV Haar cascade scans the image to find the face region

The largest detected face = license holder portrait

The face is cropped using margin values

You can download it instantly

📌 Technologies Used
Technology	Purpose
| Technology | Purpose                         |
| ---------- | ------------------------------- |
| Python     | Core programming language       |
| Streamlit  | Web UI for the app              |
| OpenCV     | Face detection + image cropping |
| NumPy      | Image array handling            |
| Pillow     | Image formatting & conversion   |
