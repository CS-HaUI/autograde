import cv2
import numpy as np
import matplotlib.pyplot as plt
from lib.threshold import auto_threshold
from lib.morphological import change_brightness, erode, dilate

def nothing(x):
    pass

def tracking_white(image, origin=None):
    # temp = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    sensitivity = 80
    lower_white = np.array([0,0,255-sensitivity])
    upper_white = np.array([255,sensitivity,255])
    mask = cv2.inRange(hsv, lower_white, upper_white)
    res = cv2.bitwise_and(image,image, mask= mask)
    return res


image = cv2.imread("dataset\\IMAGE\\004.jpg")
res = tracking_white(image)
gray = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 20, 70, 70)
img = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 113, 3)

edges_image = cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((5, 5)), iterations= 3)





# contours, hierarchy = cv2.findContours(edges_image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# print(contours)
fig, ax = plt.subplots(nrows= 1, ncols= 3)
ax[0].imshow(image[:, :, ::-1])
ax[0].axis('off')
ax[1].imshow(res[:, :, ::-1])
ax[1].axis('off')
ax[2].imshow(edges_image, cmap='gray')
ax[2].axis('off')

ax[0].set_title("Ảnh ban đầu")
ax[1].set_title("Ảnh lọc màu trắng")
ax[2].set_title("Ảnh phân ngưỡng")
plt.show()