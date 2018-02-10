import cv2
import numpy as np

filename = 'Chess1.jpg'
img = cv2.imread(filename)
gray = cv2.imread(filename, 0)
#gray = cv2.cvtColor(img,0)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray ,100,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.1*dst.max()]=[0,0,255]


cv2.namedWindow('frame',0)
cv2.imshow('frame',img)
cv2.resizeWindow('frame',800,800)

if cv2.waitKey(0) & 0xff == 'q': 
    cv2.destroyAllWindows()