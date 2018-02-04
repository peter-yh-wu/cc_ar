import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while (True):
    _, frame = cap.read()

    fgmask = fgbg.apply(frame)
    img = cv2.bitwise_and(frame, frame, mask = fgmask)

    cv2.imshow('Video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()	
