import cv2
import os
import pandas as pd
from datetime import datetime

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('Trainer/trainer.yml')

cam = cv2.VideoCapture(0)
recognized = {}
font = cv2.FONT_HERSHEY_SIMPLEX

def log_attendance(id, name):
    date = datetime.now().strftime('%Y-%m-%d')
    time_now = datetime.now().strftime('%H:%M:%S')
    filename = f"Attendance/Attendance-{date}.xlsx"
    
    if os.path.exists(filename):
        df = pd.read_excel(filename)
    else:
        df = pd.DataFrame(columns=["ID", "Name", "Date", "Time"])
    
    if not ((df["ID"] == id) & (df["Date"] == date)).any():
        df.loc[len(df)] = [id, name, date, time_now]
        os.makedirs("Attendance", exist_ok=True)
        df.to_excel(filename, index=False)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    
    for (x, y, w, h) in faces:
        id, conf = recognizer.predict(gray[y:y+h, x:x+w])
        if conf < 60:
            name = ""
            for file in os.listdir("Images"):
                if f"User.{id}." in file:
                    name = file.split(".")[2]
                    break
            cv2.putText(img, f"{name}", (x, y - 10), font, 0.8, (0, 255, 0), 2)
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            if id not in recognized:
                recognized[id] = name
                log_attendance(id, name)
        else:
            cv2.putText(img, "Unknown", (x, y - 10), font, 0.8, (0, 0, 255), 2)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow("Face Recognition", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
