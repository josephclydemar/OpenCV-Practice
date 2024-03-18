import cv2 as cv

# img = cv.imread('./Resources/Photos/group1.jpg')
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cv.imshow('Lady Original', img)
# cv.imshow('Lady Gray', gray_img)

# haar_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
# faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=1)
# print(f'Number of faces found = {len(faces_rect)}')
# for x, y, w, h in faces_rect:
#     cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

# cv.imshow('Face Detected', img)
# cv.waitKey(0)






capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
    faces_rect = haar_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=6)
    # print(f'Number of faces found = {len(faces_rect)}')
    for x, y, w, h in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
    cv.imshow('WebCAM Original', frame)

    if cv.waitKey(20) == ord('d'):
        break
capture.release()
cv.destroyAllWindows()


