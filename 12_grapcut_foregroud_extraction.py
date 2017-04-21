import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('imgData/opencv-python-foreground-extraction-tutorial.jpg')    # (281, 500, 3)
mask = np.zeros(shape=img.shape[:2], dtype=np.uint8)                            # (281, 500)

bgdModel = np.zeros(shape=(1, 65), dtype=np.float64)
fgdModel = np.zeros(shape=(1, 65), dtype=np.float64)

# rect = (161, 79, 150, 150)
# rect = (0, 0, 300, 300)
rect = (50, 50, 300, 500)

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
img = img*mask2[:, :, np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()