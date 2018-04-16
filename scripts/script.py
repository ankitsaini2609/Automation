import os
import cv2
import numpy as np
path = os.getcwd()
pathFinal = path.split('/')[4]
path = "/root/Final/"+pathFinal
os.makedirs(path)
for k in range(1, $):
    fi = 'set'+str(k)
    img = cv2.imread(fi+'/1.png')
    for i in range(1, 10, 1):
        for j in range(1, 10, 1):
            kernelOpen = np.zeros((i,i),np.uint8)
            kernelClose = np.ones((j,j),np.uint8)
            maskOpen = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernelOpen)
            maskClose = cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
            cv2.imwrite(path+"/"+fi+'_'+str(i)+'_'+str(j)+'.png',maskClose)


