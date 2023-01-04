import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank',blank)
#blank[:] = 0,255,0
cv.imshow('Green',blank)
cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_DUPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)
cv.waitKey(0)