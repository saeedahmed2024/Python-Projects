# Python-Projects
These are my some of my small-scale projects I implemented using python and its various libraries such as qrcode, opencv, pypdf etc. Take notice that these are just prototype projects. I am open to feedback/suggestions for improvements and look forward to contributing in larger scale open-source projects in the near future.
# Facial Recognition Attendance System (Python)

This project imitates a **facial-recognition–based attendance system** using Python.  
It uses a webcam to detect faces, identify known individuals, and automatically store daily attendance in a CSV file.

> ⚠️ Note: This project requires a working webcam to run successfully.

---

## 📌 Features

- Uses **face_recognition** (dlib) to encode and match faces  
- Supports multiple known users  
- Uses **OpenCV** for real-time video capture  
- Automatically logs attendance into a `{DATE}.csv` file  
- Lightweight and easy to extend

---

## 📂 Project Structure

project/
│
├── face-recognition.py # main script
├── faces/ # store known face images here
│ ├── harry.jpg
│ └── mosh.jpg
│
├── requirements.txt
├── README.md
└── .gitignore

---

## 🎥 How It Works

1. Loads known face images from the **faces/** directory.  
2. Encodes each face for recognition.  
3. Opens the webcam feed using OpenCV.  
4. Detects faces in each frame.  
5. Matches detected faces with known individuals.  
6. Creates a CSV file named with the current date:
7. Writes the recognized person’s name and timestamp.

---

## 🛠️ Installation

### 1. Clone the repository
```
git clone https://github.com/saeedahmed2024/Python-Projects.git
cd Python-Projects

```

### 2. Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows

### 3. Install dependencies
pip install -r requirements.txt

### Adding new faces 

1. Add JPEG images to the "faces" folder
2. Update the following part of the script:


new_image = face_recognition.load_image_file("faces/new_user.jpg")
new_encoding = face_recognition.face_encodings(new_image)[0]
known_face_encodings.append(new_encoding)
known_face_names.append("New User")

3. Run the script again.

### Output Example

The program generates a .csv file such as:

14-11-2025.csv

With rows such as: 

Harry, 09:41:22
Mosh, 09:42:10

### NOTE:

- This project requires a functional webcam.
- This project is built for learning purposes.
- Accuracy depends on lighting, quality of the camera and clarity of the image.
