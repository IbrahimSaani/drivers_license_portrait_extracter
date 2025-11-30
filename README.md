🪪 Driver’s License Portrait Extraction System

Automated Portrait Photo Extraction Using OpenCV & Streamlit

A lightweight, no-training-needed system that automatically extracts the portrait photo from a driver’s license image using face detection. Built with Python, Streamlit, and OpenCV.

🚀 Features

✔ Upload driver’s license image
✔ Automatically detect & crop face (portrait)
✔ Adjustable detection sensitivity
✔ View detection overlay (green box around the face)
✔ Download extracted portrait as .jpg
✔ Supports JPG / JPEG / PNG / WEBP
✔ Runs completely offline after installation
✔ Works in VS Code, PyCharm, or Streamlit Cloud

📂 Project Structure
drivers_license_portrait_extractor/
│
├─ src/
│   ├─ app.py                     # Streamlit UI
│   └─ face_extractor/
│        ├─ __init__.py
│        └─ detector.py           # OpenCV Haar-based face detection
│
├─ requirements.txt               # Install dependencies
├─ README.md
└─ .gitignore

🛠 Installation & Setup
1️⃣ Create Virtual Environment (Recommended)
python -m venv .venv

2️⃣ Activate It
Windows Powershell
.venv\Scripts\Activate.ps1

Mac / Linux
source .venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
streamlit run src/app.py


Your browser will open automatically 🌐
If not → open this link manually:
👉 http://localhost:8501

🖼 Sample Usage (Screenshot Placeholder)
Upload Image	Extracted Portrait

	

(You can replace these placeholder images later.)

⚙️ How It Works

Haar Cascade (OpenCV) detects the face →
Coordinates of the face →
Crop that region with a margin →
Display + Download image

Detection Logic – detector.py
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=scale_factor,
    minNeighbors=min_neighbors
)

🤖 Future Enhancements (Optional)
Feature	Status
OCR for license details (name, date, class, etc.)	⏳ Future update
Background removal (passport format 2x2)	⏳ Future update
Multi-language support	⏳ Future update
Desktop EXE version (auto running)	⏳ Future update
Deployment on Streamlit Cloud	🔜 Easy to do!
📌 Notes

Works best with clear, frontal driver’s license images

For OCR detection, Tesseract must be installed (we skipped this for now)

Do NOT commit .venv folder to GitHub (already ignored in .gitignore)

🙌 Credits

Built using:

Python

Streamlit

OpenCV (Haar Cascade Face Detection)