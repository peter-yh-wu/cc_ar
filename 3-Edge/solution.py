import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
    _, frame = cap.read()

    edges = cv2.Canny(frame, 200, 100)

    cv2.imshow('Edges',edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()	
