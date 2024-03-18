import cv2 as cv


# capture = cv.VideoCapture(0)
img = cv.imread('./Resources/Photos/cats.jpg')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur_img = cv.GaussianBlur(gray_img, (5, 5), cv.BORDER_DEFAULT)

# canny_img = cv.Canny(img, 125, 175)
# canny_img = cv.Canny(gray_img, 125, 175)
canny_img = cv.Canny(blur_img, 125, 175)

ret, thresh = cv.threshold(gray_img, 125, 255, cv.THRESH_BINARY)

# contours, hierarchies = cv.findContours(canny_img, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} count..')

cv.imshow('Cat Original', img)
cv.imshow('Cat Gray', gray_img)
cv.imshow('Cat Blur', blur_img)
cv.imshow('Cat Canny', canny_img)
cv.imshow('Cat Thresh', thresh)
# cv.imshow('Cat Contours', hierarchies)

cv.waitKey(0)





# while True:
#     isTrue, frame = capture.read()
#     if cv.waitKey(20) == ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

