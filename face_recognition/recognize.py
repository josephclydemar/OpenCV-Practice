import os

import cv2 as cv
import numpy as np


haar_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')


DIR = './CapturedFaces/val'

# people = ['ben_afflek', 'elton_john', 'jerry_seinfeld', 'madonna', 'mindy_kaling']
people = []
for p in os.listdir(DIR):
    people.append(p)
print(people)



face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('./face_trained.yml')

# for p in people:
#     for img in os.listdir(f'{DIR}/{p}'):
#         img_array = cv.imread(f'{DIR}/{p}/{img}')
#         gray_img_array = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
#         faces_rect = haar_cascade.detectMultiScale(gray_img_array, scaleFactor=1.1, minNeighbors=4)
#         for x, y, w, h in faces_rect:
#             faces_region_of_interest = gray_img_array[y:y+h, x:x+w]
#             label, confidence = face_recognizer.predict(faces_region_of_interest)
#             print(f'\nPerson: {people[label]}\nConfidence: {confidence}')
#             cv.rectangle(img_array, (x, y), (x+w, y+h), (0,255,0), thickness=2)
#             cv.putText(img_array, people[label], (20, 20), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0), thickness=2)
#             cv.imshow(f'{p}-{img}', img_array)
# cv.waitKey(0)


capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=9)
    for x, y, w, h in faces_rect:
        faces_region_of_interest = gray_frame[y:y+h, x:x+w]
        label, confidence = face_recognizer.predict(faces_region_of_interest)
        # print(label)
        cv.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), thickness=2)
        if confidence > 40:
            cv.putText(frame, people[label], (x, y - 20), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0), thickness=2)
        else:
            cv.putText(frame, 'unknown', (x, y - 20), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0), thickness=2)
    cv.imshow('WebCAM', frame)
    if cv.waitKey(20) == ord('d'):
            break
capture.release()
cv.destroyAllWindows()