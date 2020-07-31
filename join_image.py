import cv2
import numpy as np
img = cv2.imread("girl.png")
cv2.imshow("Girl", img)

hor = np.hstack((img, img))
cv2.imshow("hor", hor)
ver = np.vstack((img, img))
cv2.imshow("ver", ver)
cv2.waitKey(0)
