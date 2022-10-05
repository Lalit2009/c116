from email.mime import image
import cv2
image = cv2.imread("butterfly.jpg")
cv2.imshow("butterfly",image)
greyimage=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow("greyscale",greyimage)
print(image)
cv2.waitKey(0)