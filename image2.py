import matplotlib
matplotlib.use('TkAgg')
import cv2
import numpy as np

cap=cv2.VideoCapture(0)
#fourcc=cv2.VideoWriter_fourcc(*'XVID')
#out=cv2.VideoWriter('output1.avi',fourcc,20.0,(640,480))

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #out.write(frame)

    blur=cv2.GaussianBlur(gray,(5,5),0)
    edged=cv2.Canny(blur,50,200)
    cv2.imshow('frame',frame)
    cv2.imshow('edged',edged)

    if cv2.waitKey(1) & 0xFF== ord('q'):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
