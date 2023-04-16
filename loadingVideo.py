import numpy as np
import cv2

# cap = cv2.VideoCapture(0)#return video from the first webcam on your computer
#
# while (True):
#     #frame being defined as the cap.read().frame return
#     ret, frame = cap.read()# ret is a boolean regarding whether or not there was a return at all
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#showing the converted-to-gray
#     cv2.imshow('frame', frame)
#     cv2.imshow('gray', gray)#show video
#     if cv2.waitKey(1) & 0xFF == ord('q'):#key is a q, we will exit the while loop with a break
#         break
#
# cap.release()#closes all of the imshow() windows
# cv2.destroyAllWindows()#close everything


cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)#output the frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()