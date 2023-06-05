import cv2
import numpy as np
import matplotlib.pyplot as plt
from lib.threshold import auto_threshold
from lib.morphological import change_brightness, erode, dilate

image = cv2.imread("dataset\\IMAGE\\001.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


gray = cv2.bilateralFilter(gray, 20, 70, 70)

img = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 4)
edges_image = cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((5, 5)), iterations= 6)


contours, hierarchy = cv2.findContours(edges_image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



# print(contours)
print(hierarchy)


plt.imshow(edges_image, cmap='gray')
plt.axis('off')
plt.show()