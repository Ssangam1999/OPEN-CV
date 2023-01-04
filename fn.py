import cv2 as cv

img = cv.imread('images/cat.1.jpg')
cv.imshow('Cat',img)
#Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
#Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
#Edge Cascade
canny = cv.Canny(img,125,175)
cv.imshow('Canny Edges',canny)
#Dilating the image
dilated = cv.dilate(canny, (3,3),iterations=1)
cv.imshow("Dilated",dilated)
#Eroading
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded',eroded)
#resize
resized = cv.resize(img,(500,500))
cv.imshow("HEllo",resized) 
#cropped
cropped = img[50:200,200:400]
cv.imshow("cropped",cropped)

cv.waitKey(0)