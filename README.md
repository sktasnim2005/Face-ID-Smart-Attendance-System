# Face Recognition Attendance System 🎓🤖

A Python-based AI project that marks attendance using face recognition.

## 🚀 Features
- Capture face images via webcam
- Train faces using LBPH algorithm
- Recognize faces in real-time
- Log attendance in `.csv` format

## 🖥️ Technologies
- Python
- OpenCV
- NumPy, Pandas, Pillow
- Tkinter GUI

## 📦 Setup (Linux/Ubuntu)

```bash
# Clone the repo
git clone https://github.com/sktasnim2005/AI_Project.git
cd AI_Project

# Create virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install opencv-python opencv-contrib-python numpy pandas pillow

# Run the app
python main.py



## 📂 Folder Structure (auto created at runtime)
Images/       # Stores captured face images
Trainer/      # Contains trainer.yml (trained model)
Attendance/   # Logs attendance in CSV


## ✅ How to Use
1. Click **"Capture Images"**
2. Click **"Train Model"**
3. Click **"Start Attendance"** → press `q` to exit webcam


---

Created with ❤️ by [Sk Tasnim Ur Rahman](https://github.com/sktasnim2005)
