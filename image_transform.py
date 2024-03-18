import cv2 as cv
import numpy as np


def translate_frame(frame, x, y):
    # +x  -> shift right
    # -x  -> shift left
    # +y  -> shift down
    # -y  -> shift up
    translate_matrix = np.float32([[1, 0, x], [0, 1, y]])
    dims = (frame.shape[1], frame.shape[0])
    return cv.warpAffine(frame, translate_matrix, dims)


def rotate_frame(frame, angle, rotation_point=None):
    print(frame.shape)
    rows, cols, _ = frame.shape
    if rotation_point == None:
        rotation_point = (rows // 2, cols // 2)
    rotation_matrix = cv.getRotationMatrix2D(rotation_point, angle, 1.0)
    dims = (cols, rows)
    return cv.warpAffine(frame, rotation_matrix, dims)


def flip_frame(frame, flip_axis):
    return cv.flip(frame, flip_axis)

# capture = cv.VideoCapture('./Resources/Videos/dog.mp4')
capture = cv.VideoCapture(0)
# img = cv.imread('./Resources/Photos/cats.jpg')
# rotated_img = rotate_frame(img, 20)
# cv.imshow('Cat', rotated_img)
# cv.waitKey(0)





while True:
    isTrue, frame = capture.read()
    translated_frame = translate_frame(frame, -100, 100)
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rotated_frame = rotate_frame(gray_frame, 60)
    flipped_frame = flip_frame(frame, 1)
    cv.imshow('WebCAM Original', frame)
    cv.imshow('WebCAM Translated', translated_frame)
    cv.imshow('WebCAM Rotated', rotated_frame)
    cv.imshow('WebCAM Flipped', flipped_frame)
    if cv.waitKey(20) == ord('d'):
        break
capture.release()
cv.destroyAllWindows()