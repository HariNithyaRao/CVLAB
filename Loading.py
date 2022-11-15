import cv2
import numpy as np
import matplotlib.pyplot as plt

#Loading and Displaying Image

img = cv2.imread("ch.png")
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
