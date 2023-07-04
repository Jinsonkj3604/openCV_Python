import cv2
import numpy as np

image = cv2.imread('never.jpg',1)
# Converting BGR to HSV COlour Space 
hsvimage = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('hsvimage',hsvimage)
cv2.imshow('original',image)

# Then we have to track the color object so that we set the upper bound and lower bound
# of the Respective Colour Space

lower_bouhnd = np.array([110,50,50])
upper_bound = np.array([130,252,252])

# and we have to mask the objects that respective in the given range colour
# ------------
mask = cv2.inRange(hsvimage,lower_bouhnd,upper_bound)
cv2.imshow('maskedimage',mask)

# and covert to it original image using bitwise_and function

result = cv2.bitwise_and(image,image,mask=mask)
cv2.imshow('result',result)

cv2.waitKey(100000)
cv2.destroyAllWindows()
