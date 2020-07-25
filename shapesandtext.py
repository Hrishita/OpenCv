import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)
cv2.imshow("image", image)
print(image.shape)
print(image)

# color image
image[:] = 255, 0, 0
cv2.imshow("image", image)
print(image)

# range of color

image[0:100, 200:300] = 0, 255, 0
cv2.imshow("image", image)

# line
cv2.line(image, (0, 0), (300, 300), (0, 0, 255), 3)
cv2.imshow("image", image)

# full line diagonal

cv2.line(image, (0, image.shape[0]), (0, image.shape[1]), 3)
cv2.imshow("image", image)

# rectangle

cv2.rectangle(image, (0, 0), (250, 300), (0, 0, 250), 1)
cv2.imshow("image", image)
# circle
cv2.circle(image, (250, 300), 20, (255, 0, 255), 2)
cv2.imshow("image", image)
# text
cv2.putText(image, "Hello", (300, 100),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.waitKey(0)
