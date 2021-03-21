import cv2
import numpy as np

cap=cv2.VideoCapture(0)


while True:
    ret,frame=cap.read()
    if not ret:
        break
        
    cv2.imshow('frame',frame)
#     cv2.imshow('edged',edged)

    if cv2.waitKey(1) & 0xFF== ord('q'):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
