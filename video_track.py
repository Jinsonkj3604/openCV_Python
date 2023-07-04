import cv2
import numpy

cap = cv2.VideoCapture(0)

while(1):

    _,frame = cap.read()

    newimage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lwr = numpy.array([110,50,50])
    upr = numpy.array([130,252,255])

    mask = cv2.inRange(newimage,lwr,upr)
    cv2.imshow('mask',mask)

    result = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('result',result)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cv2.destroyAllWindows()