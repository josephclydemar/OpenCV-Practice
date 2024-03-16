import cv2 as cv


def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


# Can only be used for videos
def change_resolution(width, height):
    capture.set(3, width)
    capture.set(4, height)


# img = cv.imread('./Resources/Photos/cat_large.jpg')
# img = rescale_frame(img, scale=0.1)
# cv.imshow('Cat Rescaled', img)
# cv.waitKey(0)

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    frame_rescaled = rescale_frame(frame, scale=0.5)
    # change_resolution(300, 300)
    # cv.imshow('WebCAM', frame)
    cv.imshow('WebCAM-Rescaled', frame_rescaled)
    if cv.waitKey(20) == ord('d'):
        break
capture.release()
cv.destroyAllWindows()