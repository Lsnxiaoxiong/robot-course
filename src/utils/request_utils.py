import requests



class RobotTool:

    base_url = "http://192.168.137.248:5000"

    servo1 = 1600 #上下
    servo2 = 1400 #左右

    @staticmethod
    def init_head():
        RobotTool.turn_head_horizontal(1400)
        RobotTool.turn_head_vertical(1600)
        RobotTool.servo1 = 1600
        RobotTool.servo2 = 1400

    @staticmethod
    def turn_head(servo_id: int, pulse: int):
        """
        控制舵机转动到指定位置
        :param servo_id: 要驱动的舵机id(the servo id needed to be driven)
        :param pulse: 舵机目标位置(servo target position)
            上下转动的舵机限制角度在130°左右，左右180°，范围在500-2500之间。
        :return: 响应结果
        """
        url = f"{RobotTool.base_url}/robot/turn_head"
        payload = {
            "servo_id": servo_id,
            "pulse": pulse
        }
        r = requests.post(url, json=payload, timeout=10)
        return r.json()

    @staticmethod
    def turn_head_vertical(pulse: int):
        """
        控制舵机转动到指定位置
        :param pulse: 舵机目标位置(servo target position)
            上下转动的舵机限制角度在130°左右，左右180°，范围在500-2500之间。
        :return: 响应结果
        """
        url = f"{RobotTool.base_url}/robot/turn_head"
        payload = {
            "servo_id": 1,
            "pulse": pulse
        }
        r = requests.post(url, json=payload, timeout=10)
        return r.json()

    @staticmethod
    def turn_head_horizontal(pulse: int):
        """
        控制舵机转动到指定位置
        :param pulse: 舵机目标位置(servo target position)
            上下转动的舵机限制角度在130°左右，左右180°，范围在500-2500之间。
        :return: 响应结果
        """
        url = f"{RobotTool.base_url}/robot/turn_head"
        payload = {
            "servo_id": 2,
            "pulse": pulse
        }
        r = requests.post(url, json=payload, timeout=10)
        return r.json()

if __name__ == "__main__":
    r = RobotTool.turn_head_vertical(1600)
    print(r)