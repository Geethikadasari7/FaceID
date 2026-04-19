# 🚀 FaceID

- A real-time **Face Detection and Face Recognition Attendance System** built using **Python, OpenCV, and AI-based facial encoding**.
- FaceID detects faces from images/webcam and recognizes individuals to automatically mark attendance.



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



# 🔹 1. Setup for Face Detection (Basic)

## ✅ Install Dependencies

### Option 1: Using requirements.txt (Recommended)

```bash
pip install -r requirements.txt
```

### Option 2: Manual Installation

```bash
pip install opencv-python
```



## Run the Programs

```bash
python detect_face_image.py
python detect_face_video.py
```



# 🔹 2. Setup for Face Detection + Recognition (Advanced)

## ⚠️ Prerequisite

* Install **Python 3.10** (recommended for compatibility)



## ✅ Step 1: Check Python Version

```bash
py -3.10 --version
```



## ✅ Step 2: Create Virtual Environment

```bash
py -3.10 -m venv face_env
face_env\Scripts\activate
```



## ✅ Step 3: Verify Python Version

```bash
python --version
```

👉 It should display **Python 3.10.x**



# 🧩 Installation Methods (Choose One)



##  ✅ Step 4: Method 1- Using requirements.txt (Professional Way)

```bash
python -m pip install -r requirements.txt
```

👉 If any issue occurs with `dlib`, use fallback:

```bash
python -m pip install face-recognition --no-deps
python -m pip install dlib-bin
```



## ✅ Step 4: Method 2- Manual Installation (Reliable for Windows)

```bash
python -m pip install opencv-python
python -m pip install wheel
python -m pip install face-recognition --no-deps
python -m pip install Click Pillow colorama
python -m pip install dlib-bin
```



## ✅ Step 5: Run the Project

```bash
python main.py
```



## 🛑 Exit the Program

* Press **ESC** or **Q** to close the camera window
* Or press **Ctrl + C** in terminal if needed



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




# ⭐ How to Use

1. Add images of people in the `images/` folder
2. Run `main.py`
3. Show face to webcam
4. Attendance will be recorded automatically


# 📊 Output

* Detects and displays faces with names via webcam.
* Automatically records attendance in `attendance.csv`
* Works in real-time using webcam

<p align="center">
  <img src="https://github.com/user-attachments/assets/6aa4d772-2087-4432-995a-2796b4831f9b" width="40%" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://github.com/user-attachments/assets/850189e7-d5ac-490e-bb11-22d0f4df0077" width="43%" />
</p>




# 🎯 Features

* Face Detection (Image & Webcam)
* Real-time Face Recognition
* Automatic Attendance Logging
* Multi-person detection
* Easy setup with virtual environment



# 🧠 Notes

* `dlib-bin` is used instead of `dlib` to avoid build issues on Windows
* Python 3.10 is recommended for best compatibility
* Good lighting improves recognition accuracy



# 🚀 Future Enhancements

* 📊 Excel-based attendance system
* 🎨 GUI interface
* 📸 Unknown face capture
* 🧠 Confidence score display
* 🌐 Web app (React + Flask)



# 🙌 Acknowledgements

This project is my original work, developed independently using Python and OpenCV, and is intended for learning and reference purposes.

Credits:
- OpenCV
- face-recognition library
- Haar Cascade classifier (Intel Open Source License)
- Open-source resources for learning






