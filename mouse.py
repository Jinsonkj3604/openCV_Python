import cv2
image = cv2.imread('never.jpg',1)

def draw_circle(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image,(x,y),150,(0,255,255),5)

cv2.namedWindow("mousevent")
cv2.setMouseCallback('mousevent',draw_circle)

while(1):
    cv2.imshow('mousevent',image)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()