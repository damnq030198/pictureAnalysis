import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
#start coordinates, end coordinates, color (bgr), line thickness
cv2.line(img,(0,0),(200,300),(255,255,255),30)
cv2.rectangle(img,(10,25),(100,50),(0,0,255),5)
cv2.circle(img,(44,63), 63, (0,255,0), -1)
pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)
#write on the image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Tuts!',(10,130), font, 0.5, (200,255,155), 2, cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()