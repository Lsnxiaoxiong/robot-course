import cv2
import numpy as np

# 1️⃣ 读取图像
img = cv2.imread("contour.png")  # 图像中包含圆形、矩形、三角形等
cv2.imshow("Original", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# 2️⃣ 转为二值图像（阈值分割）
_, thresh = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold", thresh)

# 3️⃣ 提取轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 4️⃣ 遍历每个轮廓并判断形状
for contour in contours:
    # 计算近似多边形
    perim_px = cv2.arcLength(contour, True)  # 周长（像素单位，欧氏长度）
    # 仅用于判别形状的多边形顶点
    epsilon = 0.02 * cv2.arcLength(contour, True)

    if perim_px > 1:
        print("arcLength:", perim_px)
    # 顶点数组
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # 绘制轮廓
    cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)

    # 计算轮廓中心
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    else:
        cx, cy = 0, 0

    # 根据顶点数判断形状
    sides = len(approx)
    shape = "Unknown"
    if sides == 3:
        shape = "Triangle"
    elif sides == 4:
        # 判断矩形还是正方形
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        shape = "Square" if 0.95 < aspect_ratio < 1.05 else "Rectangle"
    elif sides > 5:
        shape = "Circle"

    # 绘制文字
    cv2.putText(img, shape , (cx - 40, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

# 5️⃣ 显示结果
cv2.imshow("Detected Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
