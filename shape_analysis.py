import cv2
import numpy as np
import matplotlib.pyplot as plt
i=cv2.imread('p1.png')
i=cv2.resize(i,(550,550))
gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
_,threshold=cv2.threshold(gray,127,240,cv2.THRESH_BINARY)
contours,_=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
c=0
for contour in contours:
    if c==0:
        c=1
        continue
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(i,[contour],0,(210,100,100),5)
    M=cv2.moments(contour)
    if M['m00']!=0.0:
        x=int(M['m10']/M['m00'])
        y=int(M['m01']/M['m00'])
    if len(approx)==3:
        cv2.putText(i,'Triangle',(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.8,(210,0,100),2)
    elif len(approx)==4:
        cv2.putText(i,'Quadrilateral',(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,100,0),2)
    elif len(approx)==5:
        cv2.putText(i,'Pentagon',(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,200,0),2)
    elif len(approx)==6:
        cv2.putText(i,'Hexagon',(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,200,0),2)
    elif len(approx)==8:
        cv2.putText(i,'Octagon',(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,200,0),2)
    else:
        cv2.putText(i,'Circle',(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,200,0),2)
cv2.imshow('Shapes',i)
cv2.waitKey(0)
cv2.destroyAllWindows()
