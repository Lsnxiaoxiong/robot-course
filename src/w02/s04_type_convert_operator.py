# 类型转换：把整型转成字符串
degree_of_freedom = 8
degree_of_freedom_str = str(degree_of_freedom)
print("机器人有 " + degree_of_freedom_str + " 个自由度")

# 基本运算符：计算机器人运动总时长
frequency = 4  # 重复4次
walk_time = 5  # 前进 5 秒
back_time = 3  # 后退 3 秒
v_m_per_s = 0.3  # 速度
print(f"机器人运行{(walk_time + back_time) * frequency}秒，"
      f"前进{(walk_time - back_time) * frequency * v_m_per_s}米，"
      f"平均前进速度为{((walk_time - back_time) * frequency * v_m_per_s) / ((walk_time + back_time) * frequency)}米/秒")
