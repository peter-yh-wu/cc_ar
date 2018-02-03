import cv2
import sys

faceCascadeFile = '/usr/local/Cellar/opencv/3.4.0_1/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(faceCascadeFile)
if faceCascade.empty(): raise Exception('bad path')

cap = cv2.VideoCapture(0)
scale = 1

while(True):
    _, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
