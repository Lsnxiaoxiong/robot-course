import threading
import time

import cv2
import numpy as np

from src.utils.request_utils import RobotTool
from src.utils.video_stream import get_frame


class ColorTracker:
    def __init__(self):

        self.cx = 240
        self.cy = 320
        self.temp_x = 0
        self.temp_y = 0
        self.lower_color = np.array([36, 35, 35])
        self.upper_color = np.array([86, 255, 255])
        self.is_tracking = False
        self.counter = 0

    def turn_head01(self):
        # time.sleep(1)
        if self.cy > 380:
            RobotTool.servo1 -= 20
            RobotTool.turn_head_vertical(pulse=RobotTool.servo1)
        elif self.cy < 240:
            RobotTool.servo1 += 20
            RobotTool.turn_head_vertical(pulse=RobotTool.servo1)

        if self.cx > 300:
            RobotTool.servo2 -= 20
            RobotTool.turn_head_horizontal(pulse=RobotTool.servo2)
        elif self.cx < 180:
            RobotTool.servo2 += 20
            RobotTool.turn_head_horizontal(pulse=RobotTool.servo2)

    def turn_head(self):
        time.sleep(3)
        RobotTool.init_head()
        while True:
            # if not self.is_tracking:
            #     RobotTool.init_head()
            #     self.cx = 240
            #     self.cy = 320
            #     RobotTool.servo1 = 1600
            #     RobotTool.servo2 = 1400
            #     time.sleep(1)
            #     continue
            # if self.counter > 10000:
            #     RobotTool.init_head()
            #     self.cx = 240
            #     self.cy = 320
            #     RobotTool.servo1 = 1600
            #     RobotTool.servo2 = 1400
            #     self.counter = 0
            #     time.sleep(1)
            #     continue
            # if self.temp_x == self.cx and self.temp_y == self.cy:
            #     time.sleep(1)
            #     continue


            if self.cy > 380:
                RobotTool.servo1 -= 100
                RobotTool.turn_head_vertical(pulse=RobotTool.servo1)
                self.counter = 0
            elif self.cy < 240:
                RobotTool.servo1 += 100
                RobotTool.turn_head_vertical(pulse=RobotTool.servo1)
                self.counter = 0

            if self.cx > 300:
                RobotTool.servo2 -= 100
                RobotTool.turn_head_horizontal(pulse=RobotTool.servo2)
                self.counter = 0
            elif self.cx < 180:
                RobotTool.servo2 += 100
                RobotTool.turn_head_horizontal(pulse=RobotTool.servo2)
                self.counter = 0

            time.sleep(1)

    def start(self):
        # threading.Thread(target=self.turn_head).start()
        RobotTool.init_head()
        for frame in get_frame(ip="192.168.1.103", port=8888):
            # frame = cv2.flip(frame, 1)
            cv2.imshow("Camera", frame)
            # print(frame.shape)  480, 640
            # BGR → HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask1 = cv2.inRange(hsv, self.lower_color, self.upper_color)

            # 提取区域
            region = cv2.bitwise_and(frame, frame, mask=mask1)

            cv2.imshow("Red Region", region)
            self.get_contour(region)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        cv2.destroyAllWindows()

    def get_contour(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if contour.shape[0] < 4:
                # self.is_tracking = False
                self.counter += 1
                print(self.counter)
                continue
            # 计算近似多边形
            perim_px = cv2.arcLength(contour, True)
            if perim_px < 130:
                # self.is_tracking = False
                self.counter += 1
                print(self.counter)
                continue
            self.is_tracking = True
            print("perim_px: ", perim_px)
            epsilon = 0.02 * perim_px
            approx = cv2.approxPolyDP(contour, epsilon, True)

            M = cv2.moments(contour)
            if M["m00"] != 0:
                self.cx = int(M["m10"] / M["m00"])
                self.cy = int(M["m01"] / M["m00"])
                self.turn_head01()
            print(f"cx: {self.cx}, cy: {self.cy}")
            # 绘制轮廓
            cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
            cv2.putText(img, f"Sides: {len(approx)}", (self.cx - 40, self.cy), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (255, 0, 0), 2)

        cv2.imshow("Detected Shapes", img)


if __name__ == "__main__":
    color_tracker = ColorTracker()
    color_tracker.start()
