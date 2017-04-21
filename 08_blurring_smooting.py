import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    # hsv hue set value
    lower_red = np.array([60, 60, 60])
    upper_red = np.array([150, 170, 160])

    # lower_red = np.array([150, 150, 50])
    # upper_red = np.array([180, 255, 150])

    # dark_red  = np.uint8([[[12, 22, 121]]])
    # dark_red = cv2.cvtColor(dark_red,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lowerb=lower_red, upperb=upper_red)
    result = cv2.bitwise_and(frame, frame, mask=mask)               # mask is return 0 or 1(boolean) in specific space

    # kernel = np.ones((15, 15), np.float32)/255
    # smooth = cv2.filter2D(result, -1, kernel)
    #
    # blur = cv2.GaussianBlur(result, (15, 15), 0)
    # medianBlur = cv2.medianBlur(result, 15)
    #
    # bilateral = cv2.bilateralFilter(result, 15, 75, 75)

    cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    # cv2.imshow('result', result)
    # cv2.imshow('smooth', smooth)
    # cv2.imshow('blur', blur)
    # cv2.imshow('medianblur', medianBlur)
    # cv2.imshow('bilateral', bilateral)



    if cv2.waitKeyEx(1) & 0xff == 27:
        break


cap.release()
cv2.destroyAllWindows()