import threading
import time
from gpiozero import Button
import hiwonder.ros_robot_controller_sdk as rrc


class TouchSensor:
    """
    触摸传感器类
    封装GPIO触摸传感器，使用子线程持续读取传感器状态
    """

    def __init__(self, pin=22, buzzer_enabled=True):
        """
        初始化触摸传感器

        Args:
            pin (int): GPIO引脚号 (BCM编号)
            buzzer_enabled (bool): 是否启用蜂鸣器反馈
        """
        self.pin = pin
        self.buzzer_enabled = buzzer_enabled

        # 初始化硬件
        self.touch = Button(pin)
        if self.buzzer_enabled:
            self.board = rrc.Board()

        # 状态变量
        self._is_touched = False
        self._prev_state = False
        self._st = 0  # 防抖状态

        # 线程控制
        self._running = False
        self._thread = None

    def start(self):
        """启动传感器监控线程"""
        if self._running:
            return

        self._running = True
        self._thread = threading.Thread(target=self._monitor_sensor)
        self._thread.daemon = True
        self._thread.start()
        print(f"Touch sensor started on pin {self.pin}")

    def stop(self):
        """停止传感器监控线程"""
        self._running = False
        if self._thread:
            self._thread.join(timeout=2.0)

        # 关闭蜂鸣器
        if self.buzzer_enabled:
            self.board.set_buzzer(1000, 0.0, 0.0, 1)
        print("Touch sensor stopped")

    def is_touched(self):
        """
        获取当前触摸状态

        Returns:
            bool: True表示被触摸，False表示未触摸
        """
        return self._is_touched

    def _monitor_sensor(self):
        """传感器监控线程的主循环"""
        while self._running:
            try:
                # 读取传感器状态
                current_state = self.touch.is_pressed
                self._is_touched = current_state

                # 蜂鸣器控制逻辑
                if self.buzzer_enabled:
                    self._handle_buzzer(current_state)

                # 避免CPU占用过高
                time.sleep(0.1)

            except Exception as e:
                print(f"Error reading touch sensor: {e}")
                time.sleep(0.5)

    def _handle_buzzer(self, current_state):
        """处理蜂鸣器反馈逻辑"""
        if current_state:  # 如果传感器被按下
            if self._st:  # 防抖判断，防止反复响
                self._st = 0
                # 以1900Hz的频率，持续响0.1秒，关闭0.9秒，重复1次
                self.board.set_buzzer(1900, 0.1, 0.9, 1)
        else:  # 如果传感器未被按下
            self._st = 1
            # 关闭蜂鸣器
            self.board.set_buzzer(1000, 0.0, 0.0, 1)

    def __enter__(self):
        """上下文管理器入口"""
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器出口"""
        self.stop()


def main():
    """测试函数"""
    # 使用上下文管理器自动管理资源
    with TouchSensor(pin=22, buzzer_enabled=True) as sensor:
        print("Touch sensor running. Press Ctrl+C to stop.")

        try:
            while True:
                # 获取当前触摸状态
                if sensor.is_touched():
                    print("Touch detected!")
                else:
                    print("No touch")

                time.sleep(1)

        except KeyboardInterrupt:
            print("\nStopping...")


if __name__ == '__main__':
    main()