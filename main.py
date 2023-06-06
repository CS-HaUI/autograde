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

cap = cv2.VideoCapture("dataset\\IMAGE\\test\\test.mp4")

if (cap.isOpened()== False):
    print("Error opening video file")

width  = 500
height = 600
# print(width)
frame_width = int(width * 2)
frame_height = int(height)
   
size = (frame_width, frame_height)
   
# Below VideoWriter object will create
# a frame of above defined The output 
# is stored in 'filename.avi' file.
result = cv2.VideoWriter('dataset\\IMAGE\\test\\output.mp4', -1, 30.0, size)

while 1:
    _, frame = cap.read()

    if _ == True:
        image = frame.copy()
        # image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        image = cv2.resize(image, (width, height))
        gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thres = valTrackbars()
        gauss = cv2.GaussianBlur(gray, (5, 5), 1)

        img_thres = cv2.Canny(gauss,200,255)


        # OPEN
        kernel = np.ones((5, 5))
        imgDial = cv2.dilate(img_thres, kernel, iterations=2)
        # imgDial = img_thres.copy()
        imgThreshold = cv2.erode(imgDial, kernel, iterations=1)
        # OPEN

        cv2.imshow('origin', image)
        cv2.imshow('output', imgThreshold)

        temp = np.concatenate((image, cv2.cvtColor(imgThreshold, cv2.COLOR_GRAY2BGR)), axis= 1)
        result.write(temp)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break
    else:
        break
result.release()
cap.release()
cv2.destroyAllWindows()