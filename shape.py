import cv2
image = cv2.imread('never.jpg',1)
cv2.line(image,(0,0),(350,350),(255,255,0),5)
cv2.rectangle(image,(200,300,200,300),(0,0,255),5)
cv2.circle(image,(150,150),150,(0,0,0),5)
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,"Hoppe Fully",(100,100),font,5,(0,0,0),4,cv2.LINE_4)
cv2.imshow('image',image)
cv2.waitKey(10000)
cv2.destroyAllWindows()
