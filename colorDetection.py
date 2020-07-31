import cv2
import numpy as np


def empty(a):
    pass


# Create Track bars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("hue min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("hue max", "TrackBars", 0, 179, empty)
cv2.createTrackbar("sat min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("sat max", "TrackBars", 153, 255, empty)
cv2.createTrackbar("value min", "TrackBars", 255, 255, empty)
cv2.createTrackbar("value max", "TrackBars", 255, 255, empty)

while True:
    img1 = cv2.imread("cards.png")
    img = cv2.resize(img1, (500, 500))
    #cv2.imshow("original", img)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # get trackbar values
    h_min = cv2.getTrackbarPos("hue min", "TrackBars")
    h_max = cv2.getTrackbarPos("hue min", "TrackBars")
    s_min = cv2.getTrackbarPos("sat min", "TrackBars")
    s_max = cv2.getTrackbarPos("sat max", "TrackBars")
    v_min = cv2.getTrackbarPos("value min", "TrackBars")
    v_max = cv2.getTrackbarPos("value max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    imgMask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=imgMask)
    cv2.imshow("hsv img", imgHSV)
    cv2.imshow("res", imgResult)

    cv2.imshow("mask", imgMask)
    cv2.waitKey(1)
