import cv2

# 读取图像
img = cv2.imread("tonypi.png")

# 转为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 显示图像
cv2.imshow("Original", img)
cv2.imshow("Gray", gray)

cv2.waitKey(0)  # 等待按键
cv2.destroyAllWindows()


