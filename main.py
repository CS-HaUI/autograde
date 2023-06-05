import cv2
import numpy as np
import matplotlib.pyplot as plt
from lib.threshold import auto_threshold
from lib.morphological import change_brightness, erode, dilate

def nothing(x):
    pass


def initializeTrackbars(intialTracbarVals=0):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Threshold1", "Trackbars", 200,255, nothing)
    cv2.createTrackbar("Threshold2", "Trackbars", 200, 255, nothing)

def valTrackbars():
    Threshold1 = cv2.getTrackbarPos("Threshold1", "Trackbars")
    Threshold2 = cv2.getTrackbarPos("Threshold2", "Trackbars")
    src = Threshold1,Threshold2
    return src

def tracking_white(image, origin=None):
    # temp = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    sensitivity = 80
    lower_white = np.array([0,0,255-sensitivity])
    upper_white = np.array([255,sensitivity,255])
    mask = cv2.inRange(hsv, lower_white, upper_white)
    res = cv2.bitwise_and(image,image, mask= mask)
    return res


initializeTrackbars()

cap = cv2.VideoCapture(0)
width  = 500
height = 600
# print(width)


while 1:
    _, frame = cap.read()

    if _ is not None:
        image = frame.copy()
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        image = cv2.resize(image, (width, height))
        gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thres = valTrackbars()
        gauss = cv2.GaussianBlur(gray, (5, 5), 1)

        img_thres = cv2.Canny(gauss,thres[0],thres[1])


        # OPEN
        kernel = np.ones((5, 5))
        imgDial = cv2.dilate(img_thres, kernel, iterations=2)
        imgThreshold = cv2.erode(imgDial, kernel, iterations=1)
        # OPEN

        cv2.imshow('origin', image)
        cv2.imshow('output', imgThreshold)

        if cv2.waitKey(1) & 0xFF == ord('x'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()