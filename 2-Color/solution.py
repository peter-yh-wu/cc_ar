import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)	
    lower_red = np.array([140,50,50])
    upper_red = np.array([180,255,255])
    maskRed = cv2.inRange(hsv, lower_red, upper_red)

    final = cv2.bitwise_and(frame, frame, mask = maskRed)

    cv2.imshow('Video Output', final)
    # cv2.imshow('Mask', maskRed)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()	
