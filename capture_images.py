import cv2
import os
import sys

if len(sys.argv) != 3:
    print("Usage: python capture_images.py <ID> <Name>")
    sys.exit(1)

Id = sys.argv[1]
name = sys.argv[2]

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
os.makedirs("Images", exist_ok=True)

sampleNum = 0

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        sampleNum += 1
        cv2.imwrite(f"Images/User.{Id}.{name}.{sampleNum}.jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img, f"Captured {sampleNum}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    cv2.imshow('Capturing...', img)
    if cv2.waitKey(1) & 0xFF == ord('q') or sampleNum >= 60:
        break

cam.release()
cv2.destroyAllWindows()
