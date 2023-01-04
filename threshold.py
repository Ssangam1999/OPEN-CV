import cv2 as cv
img = cv.imread('images/baizu.png')
cv.imshow("Baizu",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
#Simple Thresholding
threshold,thresh = cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow('Simple thresh',thresh)

threshold,thresh_inv = cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple thresh inv',thresh_inv)
#Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("Adaptive threshold", adaptive_thresh)



cv.waitKey(0)
 