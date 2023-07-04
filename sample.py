import cv2

print(cv2.__version__)
image = cv2.imread('never.jpg',1)
print(image)
# cv2.imshow('image',image)
cv2.imwrite('neverless.jpg',image)
image2 = cv2.imread('neverless.jpg',1)
cv2.imshow('newim',image2)
cv2.waitKey(1000)
cv2.destroyAllWindows()
