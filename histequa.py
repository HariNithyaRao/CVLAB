import cv2
import numpy as np
import matplotlib.pyplot as plt
i=cv2.imread('i2.jpeg',0)
e=cv2.equalizeHist(i)
r=np.hstack((i,e))
cv2.imshow("histogram image",r)
plt.plot(cv2.calcHist([i],[0],None,[250],[0,256]))
plt.plot(cv2.calcHist([r],[0],None,[250],[0,256]))
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
