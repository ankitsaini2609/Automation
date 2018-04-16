import cv2
import numpy as np
kernelOpen = np.zeros((3,3),np.uint8)
kernelClose = np.ones((3,3),np.uint8)
img = cv2.imread('2.png')
maskOpen = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernelOpen)
maskClose = cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
cv2.imwrite('new.png',maskClose)

