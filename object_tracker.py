import numpy as np
import cv2
import imutils
from collections import deque

orange_lower=(5,134,125)
orange_upper=(255,255,255)
pts=deque()
cap=cv2.VideoCapture(0)

while  True:
    ret,frame=cap.read()

    frame=imutils.resize(frame,width=600)
    blur=cv2.GaussianBlur(frame,(11,11),0)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    mask=cv2.inRange(hsv,orange_lower,orange_upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cv2.imshow("mask",mask)
    cnts=cv2.findContours(mask.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)
    center=None
    if(len(cnts)>0):
        c=max(cnts,key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        #print(x,y,M,center)

        if radius > 10:
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)
            cv2.circle(frame,center,5,(0,0,255),-1)

        pts.appendleft(center)

        for i in range(1,len(pts)):
            if(pts[i-1] is None or pts[i] is None):
                continue
            cv2.line(frame,pts[i-1],pts[i],(0,0,255),3)
            cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF== ord('q'):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
