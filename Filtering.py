import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('dog.jpeg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25
filt2D = cv2.filter2D(img, -5, kernel)
bifilt = cv2.bilateralFilter(img, 11, 75, 75)
boxfilt = cv2.boxFilter(img, 0, (5,5),img)
blur = cv2.blur(img,(7,7))
gblur = cv2.GaussianBlur(img,(5,5),0)

l = ["oimg","filt2D","bifilt","boxfilt","blur","gblur"]
imgs = [img,filt2D,bifilt,boxfilt,blur,gblur]
for i in range(6):
    plt.subplot(6,1,i+1),plt.title(l[i])
    plt.imshow(imgs[i])
    plt.xticks([]),plt.yticks([])
plt.show()
