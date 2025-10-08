import cv2
import numpy as np

# 1. 创建黑色背景图像 (512x512, 3通道, uint8)
img = np.zeros((512, 512, 3), dtype=np.uint8)

# 2. 绘制直线
cv2.line(img, (50, 100), (450, 100), (0, 255, 0), thickness=3)
# 参数说明：
# (50,100) 起点坐标
# (450,100) 终点坐标
# (0,255,0) 颜色：BGR = 绿色
# thickness=3 线宽为3像素

# 3. 绘制矩形
cv2.rectangle(img, (100, 150), (400, 300), (255, 0, 0), thickness=2)
# 若 thickness = -1 则填充矩形

# 4. 绘制圆形
cv2.circle(img, (256, 400), 50, (0, 0, 255), thickness=-1)
# thickness=-1 表示实心圆

# 5. 绘制椭圆
cv2.ellipse(img, (256, 256), (100, 50), 45, 0, 360, (255, 255, 0), 2)
# 中心点 (256,256)，长短轴(100,50)，旋转45°

# 6. 绘制多边形
pts = np.array([[100,400], [200,350], [300,400], [250,450], [150,450]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], isClosed=True, color=(255, 255, 255), thickness=2)

# 7. 添加文字
cv2.putText(img, "OpenCV Drawing Demo", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
            1, (0, 255, 255), 2, cv2.LINE_AA)
# 参数说明：
# (50,50) 文本左下角坐标
# 字体类型、字体大小、颜色、线宽、抗锯齿

# 8. 显示结果
cv2.imshow("Drawing Demo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
