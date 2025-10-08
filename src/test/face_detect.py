import cv2

#  加载人脸分类器
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

#  读取图像并转灰度
img = cv2.imread("huge.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#  检测人脸
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,  # 每次图像尺寸缩小的比例
    minNeighbors=5,  # 保留候选框的最小邻居数（越大越严格）
    minSize=(30, 30)  # 最小检测人脸尺寸
)

# 绘制检测框
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 显示结果
cv2.imshow("Detected Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
