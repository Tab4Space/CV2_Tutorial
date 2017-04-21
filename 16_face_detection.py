# Using Haar Cascade
# - xml file: define features

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('xmlFile/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('xmlFile/haarcascade_eye.xml')


cap = cv2.VideoCapture(0)


while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)      # represent face on rectangle
        region_of_image = gray[y:y+h, x:x+w]                        # only face region input new image value
                                                                    # but, 3-channel so big!, so detect eye region only gray scale
        region_of_image_color = img[y:y+h, x:x+w]                   # input region detected gray-scale

        eyes = eye_cascade.detectMultiScale(region_of_image)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(region_of_image_color, (ex, ey), (ex+ew, ey+eh), (255, 255, 0), 2)


    cv2.imshow('original', img)
    # cv2.imshow('gray', gray)
    # cv2.imshow('gray-region', region_of_image)
    # cv2.imshow('color-region', region_of_image_color)


    if cv2.waitKey(5) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()