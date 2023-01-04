import cv2 as cv
img = cv.imread('images/elu.png')

b,g,r = cv.split(img)
cv.imshow("B",b)
cv.imshow("G",g)
cv.imshow("R",r)
merged = cv.merge([b,g,r])
cv.imshow("MErged",merged)



cv.imshow("ELU",img)
cv.waitKey(0)