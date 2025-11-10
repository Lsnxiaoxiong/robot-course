import os
import sys
import time
# 替换 gpiod 库为 gpiozero 库
from gpiozero import DigitalInputDevice
import hiwonder.ros_robot_controller_sdk as rrc

if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)

board = rrc.Board()

st = 0  # 状态变量，用于防止反复响

# 使用 DigitalInputDevice 初始化引脚 24。
# 设置 pull_up=True 启用内部上拉电阻，与原代码的 gpiod.LINE_REQ_FLAG_BIAS_PULL_UP 作用一致。
# 注意：假设这里的 24 对应于 BCM 编号 24。
light = DigitalInputDevice(24, pull_up=True)

if __name__ == "__main__":
    try:
        while True:
            # 读取传感器状态。value 为 0 或 1。
            # 大多数数字光线传感器模块在感应到光线变化时会输出低电平（0）。
            state = light.value
            print(state)

            if not state:  # 如果状态为低电平（0）
                if st:  # 这里做一个判断，防止反复响
                    st = 0
                    # 以1900Hz的频率，持续响0.1秒，关闭0.9秒，重复1次
                    board.set_buzzer(1900, 0.1, 0.9, 1)
                    time.sleep(1)  # 增加的延时确保蜂鸣器响完

            else:  # 如果状态为高电平（1）
                st = 1
                # 关闭蜂鸣器
                board.set_buzzer(1000, 0.0, 0.0, 1)

                # 增加一个小的延时，避免 CPU 占用过高
            time.sleep(0.01)

    except KeyboardInterrupt:
        # 捕获键盘中断 (Ctrl+C)
        pass
    finally:
        # 无论如何，确保程序退出时关闭蜂鸣器
        board.set_buzzer(1000, 0.0, 0.0, 1)  # 关闭
        print("Program terminated.")