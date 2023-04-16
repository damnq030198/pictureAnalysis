import cv2
import numpy as np
from matplotlib import pyplot as plt

#IMREAD_COLOR  1
#IMREAD_GRAYSCALE 0
#IMREAD_UNCHANGED -1
img = cv2.imread('watch.jpg',0)#read image


# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.plot([10,300,400],[100,200,300],'c', linewidth=5)#write a line
# plt.show()

# cv2.imwrite('watchgray.png',img)#save image
#
cv2.imshow('image',img)
cv2.waitKey(0)# wait until any key is pressed
cv2.destroyAllWindows()#close everything
