

def robot_say(message):
    print("🤖 机器人:", message)

# 调用函数
robot_say("你好！我是 TonyPi")


def move_forward(steps):
    print(f"机器人前进 {steps} 步")
    return steps * 0.3  # 每步 0.3 米，返回总距离

distance = move_forward(10)
print("机器人总共移动了", distance, "米")



import time

print("机器人启动中...")
time.sleep(2)  # 延时 2 秒
print("启动完成 ✅")
