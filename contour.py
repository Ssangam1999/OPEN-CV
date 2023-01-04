import cv2 as cv
img = cv.imread('images/elu.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
ret, thresh = cv.threshold(gray,125,225,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

#contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)



cv.imshow("Elina",img)
cv.waitKey(0)
