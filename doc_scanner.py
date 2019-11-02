import cv2
from transform import four_point_transform
import numpy as np
import imutils

image=cv2.imread('/home/ekta/cv/image/get_image1.jpg')
heigth_ratio=image.shape[0]/500.0
orig=image.copy()

final_image=imutils.resize(image,height=500)
 #creating edge detector for the input image
gray=cv2.cvtColor(final_image,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)  #size of kernel, variable defining deviation in x direction
edged=cv2.Canny(blur,50,200) #minimum and maximum value set

cv2.imshow('final',edged)
cv2.waitKey(0)

cnts=cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)

cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:5]

for c in cnts:
    perimeter=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.02*perimeter,True)
    print(len(approx))
    if len(approx)==4:
        sCnt=approx
        break

cv2.drawContours(final_image,[sCnt],-1,(0,255,0),2)
cv2.imshow("outline",final_image)
cv2.waitKey(0)
warped=four_point_transform(final_image,sCnt.reshape(4,2))

cv2.imshow("warped",imutils.resize(warped,height=650))
cv2.waitKey(0)
cv2.destroyAllWindows()
