import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('imgData/messi5.jpg', cv2.IMREAD_GRAYSCALE)    # If set, always convert image to the single channel grayscale image.
                                                                # more flag => http://docs.opencv.org/trunk/d4/da8/group__imgcodecs.html

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
openCV => BGR color
matplotlib => RGB color
"""

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([50, 100], [80, 100], 'c', linewidth=5)
# plt.show()


cv2.imwrite('imgData/messi5_copy.jpg', img)
cv2.BGR