# 🚀 Face Detection and Recognition Project

A real-time **Face Detection and Face Recognition Attendance System** built using **Python, OpenCV, and AI-based facial encoding**.
This project detects faces from images/webcam and recognizes individuals to automatically mark attendance.

---

# 📂 Project Structure

```
FaceID/
│
├── Images/                  # Known faces dataset
│   ├── Geethika.jpg
│   ├── Satwik.jpg
│
├── attendance.csv          # Attendance records
├── detect_face_image.py    # Image face detection
├── detect_face_video.py    # Webcam face detection
├── main.py                 # Face recognition system
├── requirements.txt
└── README.md
```

---

# 🔹 1. Face Detection (Basic)

## ✅ Install Dependencies

### Option 1: Using requirements.txt (Recommended)

```bash
pip install -r requirements.txt
```

### Option 2: Manual Installation

```bash
pip install opencv-python
```

---

## ▶️ Run the Programs

```bash
python detect_face_image.py
python detect_face_video.py
```

---

# 🔹 2. Face Detection + Recognition (Advanced)

## ⚠️ Prerequisite

* Install **Python 3.10** (recommended for compatibility)

---

## ✅ Step 1: Check Python Version

```bash
py -3.10 --version
```

---

## ✅ Step 2: Create Virtual Environment

```bash
py -3.10 -m venv face_env
face_env\Scripts\activate
```

---

## ✅ Step 3: Verify Python Version

```bash
python --version
```

👉 It should display **Python 3.10.x**

---

# 🧩 Installation Methods (Choose One)

---

## 🚀 Method 1: Using requirements.txt (Professional Way)

```bash
python -m pip install -r requirements.txt
```

👉 If any issue occurs with `dlib`, use fallback:

```bash
python -m pip install face-recognition --no-deps
python -m pip install dlib-bin
```

---

## 🛠️ Method 2: Manual Installation (Reliable for Windows)

```bash
python -m pip install opencv-python
python -m pip install wheel
python -m pip install face-recognition --no-deps
python -m pip install Click Pillow colorama
python -m pip install dlib-bin
```

---

## ▶️ Step 5: Run the Project

```bash
python main.py
```

---

## 🛑 Exit the Program

* Press **ESC** or **Q** to close the camera window
* Or press **Ctrl + C** in terminal if needed

---

# ⚠️ Troubleshooting

If you encounter errors:

### 🔁 Reactivate environment

```bash
face_env\Scripts\activate
python main.py
```

### ❌ Face not detected

* Ensure images are clear and front-facing
* Use proper lighting

### ❌ Module not found

* Reinstall dependencies using manual method

---

# 🧠 Notes

* `dlib-bin` is used instead of `dlib` to avoid build issues on Windows
* Python 3.10 is recommended for best compatibility
* Good lighting improves recognition accuracy

---

# 🎯 Features

✔️ Face Detection (Image & Webcam)
✔️ Real-time Face Recognition
✔️ Automatic Attendance Logging
✔️ Multi-person detection
✔️ Easy setup with virtual environment

---

# 📊 Output

* Displays face bounding box with name
* Marks attendance in `attendance.csv`
* Works in real-time using webcam

---

# 💼 Description

> Developed a real-time Face Recognition Attendance System using Python, OpenCV, and facial encoding techniques to automatically identify individuals and record attendance.

---

# 🚀 Future Enhancements

* 📊 Excel-based attendance system
* 🎨 GUI interface
* 📸 Unknown face capture
* 🧠 Confidence score display
* 🌐 Web app (React + Flask)

---

# 🙌 Acknowledgements

* OpenCV
* face-recognition library
* dlib (via dlib-bin)

---

# ⭐ How to Use

1. Add images of people in the `images/` folder
2. Run `main.py`
3. Show face to webcam
4. Attendance will be recorded automatically

---

