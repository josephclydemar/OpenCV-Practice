import cv2 as cv

# capture = cv.VideoCapture('./Resources/Videos/dog.mp4')
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    grayscaled_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # Convert the Image color to Grayscale
    blurred_frame = cv.GaussianBlur(frame, (3, 3), cv.BORDER_DEFAULT) # Blur the Image
    canny_frame = cv.Canny(blurred_frame, 125, 175) # Find the Edges in the Image

    dilated_canny_frame = cv.dilate(canny_frame, (7, 7), iterations=3)
    eroded = cv.erode(dilated_canny_frame, (7, 7), iterations=3)

    resized_frame = cv.resize(frame, (400, 400), interpolation=cv.INTER_CUBIC)
    cropped_frame = frame[50:200, 200:400]

    cv.imshow('WebCAM Original', frame)
    cv.imshow('WebCAM Gray', grayscaled_frame)
    cv.imshow('WebCAM Blur', blurred_frame)
    cv.imshow('WebCAM Edges', canny_frame)
    cv.imshow('WebCAM Dilated', dilated_canny_frame)
    cv.imshow('WebCAM Eroded', eroded)
    cv.imshow('WebCAM Resized', resized_frame)
    cv.imshow('WebCAM Cropped', cropped_frame)
    if cv.waitKey(20) == ord('d'):
        break
capture.release()
cv.destroyAllWindows()