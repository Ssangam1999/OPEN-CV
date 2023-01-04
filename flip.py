import cv2 as cv
img = cv.imread('images/cat.1.jpg')
flip = cv.flip(img,-1)
cv.imshow("Flip",flip)
cv.waitKey(0)
