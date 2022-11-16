import cv2
#feature matching

img = cv2.imread('cartoon.png',cv2.IMREAD_GRAYSCALE)
imgresz = cv2.resize(img,(700,700))

siftobj = cv2.SIFT_create()
siftdt = siftobj.detect(imgresz,None)
siftimg = cv2.drawKeypoints(imgresz,siftdt,imgresz)

cv2.imshow('original', imgresz)
cv2.imshow('sift',siftimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
