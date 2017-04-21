import cv2
import numpy as np
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)                   # first webcam in my system
fourcc = cv2.VideoWriter_fourcc(*'XVID')    # video codec ...?
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      # change gray_scale

    out.write(frame)

    cv2.imshow('frame', frame)
    # cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xff == 27:       # leave only last 8-bit; 27 is ESC Key
        break


cap.release()                             # Closes video file or capturing device.
out.release()                             # quit video write
cv2.destroyAllWindows()

