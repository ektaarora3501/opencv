import cv2
import numpy as np
import math
import imutils
from collections import deque


cap = cv2.VideoCapture(0)
pts=deque()
while(1):

    #try:  #an error comes if it does not find anything in window as it cannot find contour of max area
          #therefore this try error statement

        ret, frame = cap.read()
        frame=cv2.flip(frame,1)
        kernel = np.ones((3,3),np.uint8)
   #
   #      #define region of interest
        roi=frame[200:400, 200:400]


        cv2.rectangle(frame,(200,200),(400,400),(0,255,0),0)
        blur = cv2.GaussianBlur(roi, (3,3), 0)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        lower_skin = np.array([0,20,70], dtype=np.uint8)
        upper_skin = np.array([20,255,255], dtype=np.uint8)


        # lower_skin = np.array([108, 23, 82],dtype=np.uint8)
        # upper_skin = np.array([179, 255, 255],dtype=np.uint8)

     #extract skin colur imagw
        mask = cv2.inRange(hsv, lower_skin, upper_skin)

   #

    #extrapolate the hand to fill dark spots within
        mask = cv2.dilate(mask,kernel,iterations = 4)

    #blur the image
        mask = cv2.GaussianBlur(mask,(5,5),100)

   #
   #
   #  #find contours
        cnts = cv2.findContours(mask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cnts=imutils.grab_contours(cnts)
        # print(cnts)
   #find contour of max area(hand)
        try:
            cnt = max(cnts, key =cv2.contourArea)
            epsilon = 0.0005*cv2.arcLength(cnt,True)
            approx= cv2.approxPolyDP(cnt,epsilon,True)

   #
   #  #make convex hull around hand
            hull = cv2.convexHull(cnt)
   #
   #   #define area of hull and area of hand
            areahull = cv2.contourArea(hull)
            areacnt = cv2.contourArea(cnt)

    #find the percentage of area not covered by hand in convex hull
            arearatio=((areahull-areacnt)/areacnt)*100
            font = cv2.FONT_HERSHEY_SIMPLEX
            # if l==1:
            if areacnt<2000:
                    cv2.putText(frame,'Put hand in the box',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                    print('here')
                    pts.clear()
            else:
            # print("here we will track the finger")
                    cv2.putText(frame,'1',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                # if(len(cnts)>0):
                    c=max(cnts,key=cv2.contourArea)
                    ((x, y), radius) = cv2.minEnclosingCircle(cnt)
                    M = cv2.moments(c)
                    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                    print(center)

                    if radius > 10:
                        cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)
                        cv2.circle(frame,center,5,(0,0,255),-1)
                    pts.appendleft(center)

                    for i in range(1,len(pts)):
                        if(pts[i-1] is None or pts[i] is None):
                            continue
                        cv2.line(frame,pts[i-1],pts[i],(0,0,255),3)
                    # cv2.imshow("frame",frame)






            cv2.imshow('frame',frame)

            if  cv2.waitKey(10) == ord('q'):
               break

        except:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,'Put hand in the box',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
            pts.clear()
            cv2.imshow('frame',frame)

            if  cv2.waitKey(10) == ord('q'):
               break




     #find the defects in convex hull with respect to hand
    #     hull = cv2.convexHull(approx, returnPoints=False)
    #     defects = cv2.convexityDefects(approx, hull)
    #
    # # l = no. of defects
    #     l=0
    #
    # #code for finding no. of defects due to fingers
    #     for i in range(defects.shape[0]):
    #         s,e,f,d = defects[i,0]
    #         start = tuple(approx[s][0])
    #         end = tuple(approx[e][0])
    #         far = tuple(approx[f][0])
    #         pt= (100,180)
    #
    #
    #         # find length of all sides of triangle
    #         a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    #         b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
    #         c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
    #         s = (a+b+c)/2
    #         ar = math.sqrt(s*(s-a)*(s-b)*(s-c))
    #
    #         #distance between point and convex hull
    #         d=(2*ar)/a
    #
    #         # apply cosine rule here
    #         angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
    #
    #
    #         # ignore angles > 90 and ignore points very close to convex hull(they generally come due to noise)
    #         if angle <= 90 and d>30:
    #             l += 1
    #             cv2.circle(roi, far, 3, [255,0,0], -1)
    #
    #         #draw lines around hand
    #         cv2.line(roi,start, end, [0,255,0], 2)
    #
    #
        # l+=1
    #
    #     #print corresponding gestures which are in their ranges

cap.release()
cv2.destroyAllWindows()
