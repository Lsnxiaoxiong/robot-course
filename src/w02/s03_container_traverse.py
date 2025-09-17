# 列表 (list)：机器人常用动作
robot_actions = ["前进", "后退", "挥手", "点头"]
# 遍历列表
print("🤖 机器人常用动作：")
for action in robot_actions:
    print("->", action)

# 字典 (dict)：机器人传感器数据
robot_sensors = {
    "camera": "480P分辨率摄像头",
    "舵机": "LX-824HV高压总线舵机和LFD-O1M防堵转舵机",
    "控制板": "树莓派主板和树莓派扩展板"
}
# 遍历字典
print("\n🔧 机器人传感器数据：")
for key, value in robot_sensors.items():
    print(f"{key} : {value}")

# 元组 (tuple)：机器人电池信息（电压 V,容量 mAh，电池类型）
robot_battery = ('11.1V', '2000mAh','10C锂电池')
# 遍历元组
print("\n🔋 机器人电池信息：")
for info in robot_battery:
    print("-", info)
