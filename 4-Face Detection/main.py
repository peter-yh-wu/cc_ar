import numpy as np
import cv2	
cap = cv2.VideoCapture(0)

while (True):
    _, frame = cap.read()

    # Code will Go Here

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()	
