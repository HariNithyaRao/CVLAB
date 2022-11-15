import cv2

cap=cv2.VideoCapture("myflower.mp4")
frameWidth = int(cap.get(3))
frameHeight = int(cap.get(4))
#output_mp4 = cv2.VideoWriter("VideoWriting.avi",cv2.VideoWriter_fourcc('M','J','P','G'),2,(frameWidth,frameHeight))
while True:
	ret,frame=cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#output_mp4.write(gray)
	cv2.imshow('gray',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break	
cap.release()
cv2.destroyAllWindows()
