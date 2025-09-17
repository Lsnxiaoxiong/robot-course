# 整型 (int)：机器人自由度数量
degree_of_freedom = 20
print(f"机器人有{degree_of_freedom}个自由度")

# 浮点型 (float)：机器人身高（单位：米）
robot_height = 0.373
print(f"机器人身高 {robot_height} 米")

# 布尔值 (bool)：机器人是否已开机
robot_power_on = True   # True 表示已开机，False 表示关机
print(f"机器人现在是{'开机' if robot_power_on else '关机'}状态")

# 字符串 (str)：机器人名称
robot_name = "TonyPi"
print(f'机器人名称{">"*20}{robot_name+"<"*20}')
