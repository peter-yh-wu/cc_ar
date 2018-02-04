import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)	
    lower_red = np.array([140,50,50])
    upper_red = np.array([180,255,255])
    maskRed = cv2.inRange(hsv, lower_red, upper_red)

    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(maskRed,kernel,iterations = 1)
    dilation = cv2.dilate(maskRed,kernel,iterations = 1)

    cv2.imshow('Erosion', erosion)
    cv2.imshow('Dilation', dilation)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()	
