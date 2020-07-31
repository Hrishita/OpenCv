import numpy as np
import cv2
img = cv2.imread("shape.png")
imgcountour = img.copy()


def getCountours(img):
    countours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in countours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgcountour, cnt, -1, (255, 0, 0), 2)
            peri = cv2.arcLength(cnt, True)
            print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(approx)
            print(len(approx))
            objCorner = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if objCorner == 3:
                objectType = "Tri"
            elif objCorner == 4:
                asp = w/float(h)
                if asp > 0.95 and asp < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCorner > 4:
                objectType = "Circles"
            cv2.rectangle(imgcountour, (x, y), (x+w, y+h), (0, 255, 0), 3)
            cv2.putText(imgcountour, objectType, (x+(w//2)-10, y+(h//2)-10),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getCountours(imgCanny)
imgBlank = np.zeros_like(img)
cv2.imshow("Shape", img)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Gray", imgGray)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Blank", imgBlank)
cv2.imshow("Countour", imgcountour)
cv2.waitKey(0)
