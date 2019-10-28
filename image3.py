import numpy as np
import cv2
import skimage.color as color
import skimage.segmentation as seg


img=cv2.imread('index.jpg',cv2.IMREAD_COLOR)
image_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.line(img,(0,0),(150,150),(255,255,255),15) #format bgr for white all have high intensity
#15 px wide line
cv2.rectangle(img,(20,20),(78,89),(0,0,0),5)
points=cv2.circle(img,(50,50),45,(0,255,0))
points=points.ravel()
print(points)

pts=np.array([[10,20],[50,95],[12,12]],np.int32)
cv2.polylines(img,[pts],True,(255,255,0),2)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Trying on OPencv',(0,100),font,0.80,(0,200,100),4,cv2.LINE_AA)
#first size and next is  thickness

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
