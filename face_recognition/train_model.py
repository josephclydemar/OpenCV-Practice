import os
# import time
import numpy as np
import cv2 as cv


haar_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')


DIR = './CapturedFaces/train'

people = []
for p in os.listdir(DIR):
    people.append(p)
# print(people)


def train_face_recognizer():
    features = []
    labels = []

    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray_img_array = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            # faces_rect = haar_cascade.detectMultiScale(gray_img_array, scaleFactor=1.1, minNeighbors=4)
            # for x, y, w, h in faces_rect:
            #     faces_region_of_interest = gray_img_array[y:y+h, x:x+w]
            features.append(gray_img_array)
            labels.append(label)
    
    features = np.array(features, dtype='object')
    labels = np.array(labels)

    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.train(features, labels)

    np.save('./parameters/features.npy', features)
    np.save('./parameters/labels.npy', labels)

    face_recognizer.save('face_trained.yml')
    print('Traing Finished--------------------------')




if __name__ == '__main__':
    train_face_recognizer()





# name = input('Enter your name: ')
# capture_new_images(name, 50)




