import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([30, 10, 50])
    upper_red = np.array([255, 255, 180])
    #nếu trong khoang thì chuyển sang trắng còn lại là đen
    mask = cv2.inRange(hsv, lower_red, upper_red)
    #and với bức and gốc
    res = cv2.bitwise_and(frame, frame, mask=mask)
    #chuyển đổi BGR sang HSV
    dark_red = np.uint8([[[12, 22, 121]]])
    dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)
    #tạc mảng toàn 1 vs kích cỡ 15x15  kiểu float 32
    kernel = np.ones((15, 15), np.float32) / 225
    #làm mịn
    smoothed = cv2.filter2D(res, -1, kernel)
    cv2.imshow('Original', frame)
    cv2.imshow('Averaging', smoothed)
    # làm mờ Gaussian
    blur = cv2.GaussianBlur(res, (15, 15), 0)
    cv2.imshow('Gaussian Blurring', blur)
    #Median Blur
    median = cv2.medianBlur(res, 15)
    cv2.imshow('Median Blur', median)
    #mờ hai bên
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)
    cv2.imshow('bilateral Blur', bilateral)
    # cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    # cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k == ord('a'):
        break

cv2.destroyAllWindows()
cap.release()