import cv2
import numpy as np
from PIL import Image
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'Images'

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []
    
    for imagePath in imagePaths:
        gray_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(gray_img, 'uint8')
        id = int(os.path.split(imagePath)[-1].split('.')[1])
        faces = face_cascade.detectMultiScale(img_numpy)
        
        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y+h, x:x+w])
            ids.append(id)
    return faceSamples, ids

print("[INFO] Training model. This may take a few seconds...")
faces, ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

os.makedirs("Trainer", exist_ok=True)
recognizer.write('Trainer/trainer.yml')
print("[SUCCESS] Model trained and saved as Trainer/trainer.yml")
