import cv2
import numpy as np
import matplotlib.pyplot as plt
i=cv2.imread('img.jpeg',-1)
gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
img=cv2.GaussianBlur(gray,(3,3),0)
sobelx=cv2.Sobel(i,cv2.CV_64F,1,0,ksize=5)
sobely=cv2.Sobel(i,cv2.CV_64F,0,1,ksize=5)
edge=cv2.Canny(i,50,150,apertureSize=3)
edge1=cv2.Canny(i,50,150,apertureSize=5)
edge2=cv2.Canny(i,50,150,apertureSize=7)
imgs = [img,sobelx,sobely,edge,edge1,edge2]
titles = ['img','sobelx','sobely','edge','edge1','edge2']
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.title(titles[i])
    plt.imshow(imgs[i])
    plt.xticks([]),plt.yticks([])
plt.show()


