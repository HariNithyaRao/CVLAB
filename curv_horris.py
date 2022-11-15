import cv2
import numpy as np
i1=cv2.imread('p2.png')
i=cv2.imread('p2.png')
gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
img_flt=np.float32(gray)
dst=cv2.cornerHarris(img_flt,2,3,0.04)
dst=cv2.dilate(dst,None)
i[dst>0.01*dst.max()]=[0,0,255]
cv2.imshow('ori',i1)
cv2.imshow('Detected Corners',i)
cv2.waitKey(0)
cv2.destroyAllWindows()
