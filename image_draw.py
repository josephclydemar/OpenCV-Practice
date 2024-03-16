import cv2 as cv
import numpy as np


blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank Black Image', blank)

# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Red Square', blank)

# blank[:] = 0, 255, 255
# cv.imshow('Blank Green Image', blank)

cv.rectangle(blank, (150, 50), (350, 250), (0, 255, 0), thickness=2)
cv.putText(blank, 'Hellooww Yoo!! My name is Clyde', (25, 225), cv.FONT_HERSHEY_TRIPLEX, 0.75, (0, 0, 255), 2)
cv.imshow('Rectangle', blank)

cv.waitKey(0)