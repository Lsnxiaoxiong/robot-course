import cv2

img = cv2.imread("tonypi.png")
small = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# 指定大小 (宽, 高)
resize_200x200 = cv2.resize(img, (200, 200))

cv2.imshow("Resize Small", small)
cv2.imshow("Resize 200x200", resize_200x200)
cv2.waitKey(0)