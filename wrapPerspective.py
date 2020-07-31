import numpy as np
import cv2
img = cv2.imread("cards.png")
width, height = 250, 350
pts1 = np.float32([[1317, 133], [2473, 457], [901, 1705], [2103, 2021]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imageOut = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("cards", imageOut)

cv2.waitKey(0)
