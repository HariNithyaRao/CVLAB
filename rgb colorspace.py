import cv2
import numpy as np
image = cv2.imread("dog.jpeg")

img = image.astype(np.float64)/255.
K = 1 - np.max(img, axis=2)
C = (1-img[...,2] - K)/(1-K)
M = (1-img[...,1] - K)/(1-K)
Y = (1-img[...,0] - K)/(1-K)

CMYK_image= (np.dstack((C,M,Y,K)) * 255).astype(np.uint8)
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("Original Image", image)
cv2.imshow("CMYK Image", CMYK_image)
cv2.imshow("HSV",hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
