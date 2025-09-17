robot_battery_level = 25  # 电池电量百分比

if robot_battery_level < 20:
    print("⚠️ 电量不足，请及时充电！")
else:
    print("✅ 电量充足，可以继续运行")


# for 循环：执行一组动作
actions = ["站立", "前进", "挥手"]
for act in actions:
    print("执行动作:", act)

# while 循环：机器人连续行走，直到到达目标点
distance = 0
while distance < 5:
    print("机器人向前走一步")
    distance += 1
print("机器人到达目标点")


# 模拟机器人在两层楼中巡逻
floors = [1, 2]
rooms = ["01", "02", "03"]

for f in floors:
    for r in rooms:
        r = str(f) + r
        if r == "202" and f == 2:
            print("遇到障碍物，跳过房间", r)
            continue
        if r == "203" and f == 2:
            print("紧急任务，结束巡逻！")
            break
        print(f"机器人正在巡逻 {f} 楼 {r} 房间")