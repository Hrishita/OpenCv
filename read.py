import cv2
import numpy as np
kernal = np.ones((3, 3), np.uint8)
imageRead = cv2.imread("girl.png")
cv2.imshow("girl", imageRead)
imageBlur = cv2.GaussianBlur(imageRead, (7, 7), 0)
cv2.imshow("Blur", imageBlur)
imageCanny = cv2.Canny(imageBlur, 100, 150)
cv2.imshow("Canny", imageCanny)
imageDialation = cv2.dilate(imageCanny, kernal, iterations=1)
cv2.imshow("Dialation", imageDialation)
imageErosion = cv2.erode(imageDialation, kernal, iterations=1)
cv2.imshow("Erosion", imageErosion)
cv2.waitKey(0)
