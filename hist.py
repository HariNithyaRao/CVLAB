import cv2
from matplotlib import pyplot as plt
img=cv2.imread('i2.jpeg',0)
cv2.imshow("Image",img)
hist=cv2.calcHist([img],[0],None,[250],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.plot(hist)
plt.show()
