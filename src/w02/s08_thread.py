import hiwonder.ActionGroupControl as AGC
import hiwonder.ros_robot_controller_sdk as rrc
from hiwonder.Controller import Controller
import threading
import time

board = rrc.Board()
ctl = Controller(board)

def worker(servo_id, pulse):
    ctl.set_pwm_servo_pulse(servo_id, pulse, 1000)

# 创建线程
t1 = threading.Thread(target=worker, args=(1, 1700))
t2 = threading.Thread(target=AGC.runAction, args=("go_forward_one_step",))

t1.start()
t2.start()

t1.join()  # 等待 t1 执行完成
t2.join()
print("执行完成")