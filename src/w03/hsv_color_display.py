import cv2
import numpy as np

# 图像大小：宽=H(0-179)，高=S(0-255)
width, height = 180, 256

# 创建 HSV 平面图
hsv = np.zeros((height, width, 3), dtype=np.uint8)

for y in range(height):       # S 方向
    for x in range(width):    # H 方向
        hsv[y, x, 0] = x       # 色相 H
        hsv[y, x, 1] = y       # 饱和度 S
        hsv[y, x, 2] = 255     # 亮度 V 固定为最大

# 转换为 BGR 图像
bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# 鼠标点击事件
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        h_val = hsv[y, x, 0]
        s_val = hsv[y, x, 1]
        v_val = hsv[y, x, 2]

        b_val = bgr[y, x, 0]
        g_val = bgr[y, x, 1]
        r_val = bgr[y, x, 2]

        print(f"位置=({x},{y}) | HSV=({h_val}, {s_val}, {v_val}) | BGR=({b_val}, {g_val}, {r_val})")

# 创建窗口并绑定事件
cv2.namedWindow("HSV Plane")
cv2.setMouseCallback("HSV Plane", mouse_callback)

cv2.imshow("HSV Plane", bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
