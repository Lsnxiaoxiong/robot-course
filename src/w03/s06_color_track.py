import cv2
import numpy as np

def get_contour(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        # 计算近似多边形
        perim_px = cv2.arcLength(contour, True)
        if perim_px < 80:
            continue
        epsilon = 0.02 * perim_px
        approx = cv2.approxPolyDP(contour, epsilon, True)

        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
        else:
            cx, cy = 0, 0

        # 绘制轮廓
        cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
        cv2.putText(img, f"Sides: {len(approx)}", (cx - 40, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    cv2.imshow("Detected Shapes", img)


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Camera", frame)

        # 读取图像
        # img = cv2.imread(frame)

        # BGR → HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 红色范围（低阈值 & 高阈值）
        lower_red = np.array([36, 35, 35])
        upper_red = np.array([86, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)
        #
        # lower_red = np.array([170, 120, 70])
        # upper_red = np.array([180, 255, 255])
        # mask2 = cv2.inRange(hsv, lower_red, upper_red)

        # 合并两个红色区间
        # mask = mask1 + mask2

        # 提取红色区域
        red_region = cv2.bitwise_and(frame, frame, mask=mask1)

        cv2.imshow("Red Region", red_region)
        get_contour(red_region)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()