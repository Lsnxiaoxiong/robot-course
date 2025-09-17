class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery  # 电池电量

    def speak(self, msg):
        print(f"{self.name} 说:", msg)

    def charge(self, amount):
        self.battery += amount
        print(f"{self.name} 已充电，现在电量 {self.battery}%")

# 实例化一个机器人
robot = Robot("TonyPi", 50)
robot.speak("大家好，我是TonyPi！")
robot.charge(30)
