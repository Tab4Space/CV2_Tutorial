import cv2
import numpy as np

img1 = cv2.imread('imgData/3D-Matplotlib.png')
img2 = cv2.imread('imgData/mainsvmimage.png')
img3 = cv2.imread('imgData/mainlogo.png')

# add = img1 + img2
# add = cv2.add(img1, img2)
# cv2.imshow('add', add)

# weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
# cv2.imshow('weight', weighted)

rows, cols, channels = img3.shape
print rows, cols, channels
region_of_image = img1[0:rows, 0:cols]
cv2.imshow('reg', region_of_image)


# img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
# cv2.imshow('img3gray', img3gray)
# # if pixel value is great then threshold, it is assigned one value
# # cv2.THRESH_BINARY_INV: change 2 color(black, white), and inverse setted value
# ret, mask = cv2.threshold(img3gray, 220, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('mask', mask)

img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img3gray, 220, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(region_of_image, region_of_image, mask=mask_inv)
img2_fg = cv2.bitwise_and(img3, img3, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst
cv2.imshow('res', img1)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img2_fg', img2_fg)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()