import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cartoon.png')
_,mask = cv2.threshold(img , 210,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((2,2),np.uint8)
dilate = cv2.dilate(mask,kernel)
erode = cv2.erode(mask,kernel)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
close = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
titles = ['oimg','maskimg','dilated','eroded','opening','closing']
imgs = [img,mask,dilate,erode,opening,close]
for i in range(6):
    plt.subplot(3,2,i+1)
    plt.title(titles[i])
    plt.imshow(imgs[i])
    plt.xticks([]),plt.yticks([])
plt.show()
