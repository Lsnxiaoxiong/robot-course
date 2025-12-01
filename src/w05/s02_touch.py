import os
import sys
import time
# 替换 gpiod 库为 gpiozero 库
from gpiozero import Button
import hiwonder.ros_robot_controller_sdk as rrc

board = rrc.Board()

st = 0  # 状态变量，用于防止反复响
# 使用 Button 类初始化引脚 22。Button 默认启用内部上拉电阻，并处理为按下时为 True (低电平触发)。
# 注意：假设这里的 22 对应于 BCM 编号 22。
touch = Button(22)

if __name__ == '__main__':
    try:
        while True:
            # 读取传感器状态。touch.is_pressed 在传感器被按下(低电平)时返回 True
            state = touch.is_pressed

            if state:  # 如果传感器被按下 (对应原代码 if not state:)
                if st:  # 这里做一个判断，防止反复响
                    st = 0
                    # 以1900Hz的频率，持续响0.1秒，关闭0.9秒，重复1次
                    board.set_buzzer(1900, 0.1, 0.9, 1)
            else:  # 如果传感器未被按下 (对应原代码 else:)
                st = 1
                # 关闭蜂鸣器
                board.set_buzzer(1000, 0.0, 0.0, 1)

                # 增加一个小的延时，避免 CPU 占用过高
            time.sleep(0.1)

    except KeyboardInterrupt:
        # 捕获键盘中断 (Ctrl+C)
        pass
    finally:
        # 无论如何，确保程序退出时关闭蜂鸣器
        board.set_buzzer(1000, 0.0, 0.0, 1)  # 关闭
        print("Program terminated.")