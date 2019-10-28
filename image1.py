import matplotlib
import numpy as np
matplotlib.use('TkAgg')
import time
import matplotlib.pyplot as plt
import cv2
import sys


img=cv2.imread("/home/ekta/cv/t2.jpg",cv2.IMREAD_GRAYSCALE)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#fig,ax=plt.subplots(nrows=nrows,ncols=ncols,figsize=(14,14))

plt.imshow(img,cmap='gray')
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show()
