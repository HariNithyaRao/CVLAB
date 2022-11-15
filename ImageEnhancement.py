from PIL import Image,ImageEnhance
import matplotlib.pyplot as plt
import cv2

img = Image.open('images.jpeg')
#img.show()
obri = ImageEnhance.Brightness(img)
ebri = obri.enhance(3.45)
#ebri.show()

ocolor = ImageEnhance.Color(img)
ecolor = ocolor.enhance(78)
#ecolor.show()

ocontrast = ImageEnhance.Contrast(img)
econtrast = ocontrast.enhance(3.56)
#econtrast.show()

osharp = ImageEnhance.Sharpness(img)
esharp = osharp.enhance(6.7)
#esharp.show()

titles = ['ebri', 'ecolor','econtrast','esharp']
imgstack = [ebri, ecolor,econtrast,esharp]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.title(titles[i])
    plt.imshow(imgstack[i])
plt.show()
    
