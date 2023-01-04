import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('images/elu.png')
cv.imshow('Elina',img)
plt.imshow(img)
plt.show()
#BGR TO HSV
#hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
#cv.imshow('HSV',hsv)
#BGR TO LAB
#BGR TO HSV
#lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
#cv.imshow('HSV',lab)

cv.waitKey(0)