import numpy as np
import cv2

cap = cv2.VideoCapture('people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while (1):
    ret, frame = cap.read()
    # so sánh hai hình ảnh tương tự và ngay lập tức trích xuất sự khác biệt giữa chúng
    fgmask = fgbg.apply(frame)

    cv2.imshow('fgmask', frame)
    cv2.imshow('frame', fgmask)

    k = cv2.waitKey(30)
    if k == ord('a'):
        break

cap.release()
cv2.destroyAllWindows()