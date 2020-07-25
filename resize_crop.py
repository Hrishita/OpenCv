import cv2
img = cv2.imread("fruits.png")
print(img.shape)
cv2.imshow("Fruits", img)

imgResize = cv2.resize(img, (300, 300))
print(imgResize.shape)
cv2.imshow("Fruits1", imgResize)

imgCrop = img[0:200, 100:300]
print(imgCrop.shape)
cv2.imshow("Cropped", imgCrop)

cv2.waitKey(0)
