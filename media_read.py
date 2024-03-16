import cv2 as cv

# # Reading images
# img = cv.imread('./Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)

# Reading Videos
# capture = cv.VideoCapture('./Resources/Videos/dog.mp4')
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Dog', frame)
    mystery = cv.waitKey(20)
    # print(mystery, mystery & 255)
    # if mystery & 0xFF == ord('d'): #? Why bitwise AND  this (cv.waitKey(20) with 0xFF) ?
    #     break
    if mystery == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


