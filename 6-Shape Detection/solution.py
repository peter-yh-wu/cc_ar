import numpy as np
import math
import cv2	

cap = cv2.VideoCapture(0)

while (True):
    _, frame = cap.read()
    canny = cv2.Canny(frame, 40, 100, 2)
    _, contours, _ = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    print(len(contours))

    for i in range(0,len(contours)):
        approx = cv2.approxPolyDP(contours[i],cv2.arcLength(contours[i],True)*0.02,True)
    
        if len(approx)==3:
            print("triangle")
            cv2.drawContours(frame,[contours[i]],0,(0,255,0),-1)
        elif len(approx)==4:
            print("rectangle")
            cv2.drawContours(frame,[contours[i]],0,(0,0,255),-1)
        elif len(approx) > 15:
            print("circle")
            cv2.drawContours(frame,[contours[i]],0,(0,255,255),-1)


    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()	
