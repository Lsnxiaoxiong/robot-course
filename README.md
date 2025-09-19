**机器人课程（共11周）**

# 技术导论与环境搭建（第1周）



## 课程介绍与计划

### 课程简介

本课程是一门面向本科生的选修课程，以幻尔 **TonyPi-Pro 人形机器人** 为主要教学平台，带领同学们系统学习人形机器人相关的理论与实践技术。课程涵盖机器人机械结构、运动控制、计算机视觉、语音交互、传感器应用以及人工智能大模型整合，旨在帮助学生掌握“软硬结合”的综合开发能力。



### 课程特色

**理论与实践结合**：课程从人形机器人的发展历程出发，深入讲解驱动、感知、控制和智能等核心技术，并结合 TonyPi-Pro 的实际实验操作，让知识“落地”。

**多模态交互体验**：同学们将学习如何让机器人“看、听、说、动”，实现基于视觉、语音和传感器的智能交互。

**AI赋能机器人**：课程特别引入 **YOLO目标检测**、**大语言模型 (LLM)** 以及 **MCP工具调用** 等前沿技术，探索具身智能的最新进展。

**项目驱动学习**：从田径跨栏、智能搬运到自主创新作品设计，课程通过项目实践激发学生的创造力和工程能力。



### 课程模块

**第一周：技术导论与环境搭建**
我们将从人形机器人的发展简史、应用场景及核心技术讲起，并指导你完成TonyPi Pro机器人的开发环境准备工作。

**第二周：Python与机器人基本控制**
本周将快速掌握Python编程基础，并学习如何通过代码控制TonyPi Pro的舵机，实现行走、抓握、转头等基本动作。

**第三周：OpenCV与机器人视觉**
我们将深入计算机视觉的世界，学习图像处理技术，让机器人能够识别颜色、检测形状和追踪动态目标。

**第四周：机器人语音识别与语音合成**
为机器人安装并调试语音模块，通过语音指令控制机器人，并尝试结合视觉进行颜色识别与语音播报。

**第五周：机器人传感器**
你将学习如何使用触摸、超声波、光线等多种传感器，让机器人具备更丰富的环境感知能力。

**第六周：机器人AI模块**
进入激动人心的人工智能模块，你将了解并实践YOLO目标检测，并初步接触大语言模型（LLM）的基本原理与调用方法。

**第七周：智能搬运与田径跨栏**
在这一周，我们将挑战更复杂的综合任务，如智能巡线、爬台阶和跨栏运动，检验机器人的运动控制与环境感知能力。

**第八周：大模型与机器人整合**
我们将探讨如何设计一个整合大语言模型的机器人系统，并以语音或手势控制为例，让你感受“具身智能”的魅力。

**第九至十周：综合实践**
这是你大展身手的机会！你可以选择挑战“田径跨栏+物品搬运”的指定任务，或自主设计一个融合本课程所学技术的创意作品，作为你的结课大作业。

**第十一周：作品展示**
在课程的最后，你将向所有同学展示你的最终作品，分享你的创意、成果与心得。



### 教学目标

+ 掌握人形机器人的基本原理与核心技术；

+ 独立完成基于 Python 的机器人程序设计；

+ 将计算机视觉、语音识别与传感器应用融入机器人交互；

+ 将人工智能大模型与机器人结合，探索具身智能应用；

+ 团队协作完成综合性机器人创新项目，并进行展示。



## 引言

同学们好，欢迎选修《人形机器人技术导论》这门课程。

如果说计算机、智能手机和新能源汽车定义了过去的数十年，那么人形机器人，这一集人工智能、高端制造、新材料等前沿技术于一体的结晶，正蓄势待发，成为开启未来的关键。本课程将作为你们的向导，共同探索这个令人兴奋的新兴领域。



### **一、 从科幻到现实：人形机器人的发展简史**

人形机器人的梦想由来已久，其发展历程大致可分为三个关键阶段：

- **早期探索 (1970s-2000s)：** 一切始于实验室中的蹒跚学步。从日本早稻田大学的全球首台全尺寸人形机器人 **WABOT-1** 证明可行性，到本田公司的 **ASIMO** 以其流畅的行走能力惊艳世界，这个阶段的先驱者们为机器人的稳定步行奠定了理论基础。

![image-20250905111855818](README_assets/image-20250905111855818.png)



- **技术突破 (2000s-2020)：** 这是属于“网红”机器人的时代。以波士顿动力公司的 **Atlas** 为代表，机器人展示了跑酷、后空翻等惊人的动态平衡与运动能力，极大地突破了人们对机器运动极限的想象。同时，机器学习技术开始融入，让机器人具备了初步的学习和适应能力。

![image-20250905112149386](README_assets/image-20250905112149386.png)



[![image-20250905121939715](README_assets/image-20250905121939715.png)](https://www.bilibili.com/video/BV1ay4y1D7WM/?spm_id_from=333.337.search-card.all.click&vd_source=916449cf2555535fc5fea68741c33019)

- **产业化加速 (2020-至今)：** 我们正处在这个激动人心的时代。随着以 **ChatGPT** 为代表的**大语言模型 (LLM)** 和 **“具身智能”** 概念的爆发，机器人迎来了“智慧大脑”的革命性升级。特斯拉的 **Optimus** 、宇树科技的G1等产品正加速从实验室走向工厂和现实生活，预示着一个人形机器人产业化的新纪元已经到来。

![image-20250905132948354](README_assets/image-20250905132948354.png)

![image-20250905132741504](README_assets/image-20250905132741504.png)

特斯拉Optimus 

[![image-20250905132452488](README_assets/image-20250905132452488.png)](https://www.bilibili.com/video/BV1VxJqzfELu/?spm_id_from=888.80997.embed_other.whitelist&t=56.333447&bvid=BV1VxJqzfELu)



宇树G1机器人

[![image-20250905132253378](README_assets/image-20250905132253378.png)](https://www.bilibili.com/video/BV14XaHzuEkM/?spm_id_from=888.80997.embed_other.whitelist&bvid=BV14XaHzuEkM)

 



### **二、 不止于工厂：人形机器人的广阔应用场景**

人形机器人拥有与人类相似的形态，这使其能够无缝融入为人类设计的环境中，应用潜力巨大：

- **智能制造：** 在汽车、电子等生产线上，它们将代替人类完成重复性、高精度的装配、搬运与质检工作。
- **社会服务：** 在商场、酒店、医院等场所，它们可以担任导购、接待、陪护等角色，提供人性化的服务。
- **医疗康复：** 它们可以作为康复训练的助手，辅助老年人起居，甚至在未来参与到精密的手术辅助中。
- **极限探索：** 在太空、深海、灾后救援等高危环境中，人形机器人将代替人类执行勘探、维修和救援任务，保障生命安全。



### **三、 揭秘核心：驱动机器人的关键技术**

要让一台机器人像人一样行动和思考，背后是一个复杂而精妙的技术体系。我们可以将其简化为四大核心部分：

1. **强健的“身躯”—— 机械结构与材料：** 这是机器人的骨骼与肌肉。通过仿生设计、轻量化材料（如碳纤维）和高精度的驱动器（电机、减速器），实现机器人灵活而有力的运动。
2. **敏锐的“感官”—— 感知系统：** 这是机器人的眼睛和皮肤。依靠**视觉（摄像头）、力觉与触觉传感器**等多传感器融合技术，机器人能够精准感知并理解周围的三维世界。
3. **协调的“小脑”—— 运动控制：** 这是机器人平稳行走和操作的关键。核心算法致力于解决**双足步行、动态平衡和全身协调**等难题，确保机器人在复杂地形中也能行动自如。
4. **智能的“大脑”—— 人工智能与认知：** 这是人形机器人的灵魂。近年来，随着**大语言模型 (LLM)** 和**具身智能**技术的发展，机器人不仅能“听懂”人类的复杂指令，还能进行推理、规划任务，并从与环境的交互中不断学习。



本课程将带领大家深入探索以上这些激动人心的领域。我们不仅会学习理论知识，更会通过实践项目，让大家对人形机器人的设计、控制与应用有一个直观的认识。这不仅是一门前沿的技术课程，更是一次通往未来的探索之旅。

 



## 幻尔TonyPi-Pro机器人简介

TonyPi Pro是幻尔科技开发的一款人形机器人。[官网](https://www.hiwonder.com.cn/product-detail/TonyPi-Pro.html)

![image-20250916104928877](README_assets/image-20250916104928877.png)

### 基本信息

TonyPi Pro基于树莓派5B开发，它在TonyPi机器人的基础上做了很多升级，使得TonyPi。 Pro不仅保留了之前所有的功能，还拓展出了更多有趣的AI创意玩法，如跨栏越障、上下台阶、智能抓取、口罩识别、多台群控等等。它不仅能满足用户对机器视觉、机器人运动学等算法的学习和验证，还为传感器应用、视觉抓取等二次开发提供快速、便捷的集成方案。                    



### 参数详情

| 硬件/系统          | 参数/版本                                                    |
| :----------------- | :----------------------------------------------------------- |
| 机体尺寸           | 高度*肩宽*厚度 373x187x106mm                                 |
| 机体重量           | 约1.8kg(不含开合手掌)                                        |
| 机体材料           | 硬铝合金                                                     |
| 摄像头分辨率       | 480P                                                         |
| 电池               | 11.1V 2000mAh 10C锂电池                                      |
| 续航时间           | 持续运行约1小时                                              |
| 自由度             | 20个DOF                                                      |
| 控制系统           | 树莓派4B（4G内存）和树莓派扩展板                             |
| 配套软件           | 手机APP+PC端上位机+PC端控制软件                              |
| 通信方式           | Wi-Fi、以太网                                                |
| 舵机参数           | LX-824HV 高压总线舵机 堵转扭矩：17kg/cm 11.1V； LFD-01M防堵转舵机 堵转扭矩：1.5kg/cm 4.8V； |
| 控制方式           | PC端控制/手机APP控制/手柄控制                                |
| 包装尺寸           | 长度*宽度*高度 560*360*310mm                                 |
| 整体重量（含包装） | 约4.5kg                                                      |



### 启动机器人

#### 接线

> 先检测机器人的充电线是否接线（机器人左臂下方），如未接线，先进行接线，完成如下图。

![image-20250916110152190](README_assets/image-20250916110152190.png)



#### 开关机

将机器人背面底部的树莓派扩展板开关由“**OFF**”推动到“**ON**”，此时扩展板的LED1、LED2将常亮，设备开机成功后，蜂鸣器会“嘀”的一声

![image-20250916110921218](README_assets/image-20250916110921218.png)

![image-20250916110952446](README_assets/image-20250916110952446.png)

#### 电量

TonyPi背部搭载了一个电压显示模块，可实时观察机器人当前电量情况，如下图示：

![image-20250916111104462](README_assets/image-20250916111104462.png)



#### 充电

将充电器插入充电口。TonyPi的工作电压范围大小为9V-12.6V，当电量充满时，电压显示模块会显示“**12.6**”，当前电压小于10V时，请及时给机器人充电。

![image-20250916121513660](README_assets/image-20250916121513660.png)



### 连接机器人

#### 远程桌面连接

[启动机器人](#启动机器人)，机器人启动完成之后会开启一个HW开头的热点，密码为**hiwonder**。使用电脑连接该热点。

![image-20250916115853483](README_assets/image-20250916115853483.png)

参考[软件环境安装文档](./docs/01_dev_env.md)中[VNC-Viewer](./docs/01_dev_env.md/#VNC-Viewer)安装远程桌面连接软件，打开。

在打开的 VNC Viewer 中输入树莓派默认的 IP 地址：192.168.149.1，然后按回车

![image-20250916120013340](README_assets/image-20250916120013340.png)

此时弹出一个提示框，要求输入账号（Username）和密码（Password）

+ 账号：pi
+ 密码：raspberrypi

![image-20250916120128230](README_assets/image-20250916120128230.png)



连接成功后如下图：

![image-20250916120159514](README_assets/image-20250916120159514.png)



#### 手机app连接

[官网](https://www.hiwonder.com.cn/downloads.html)下载安装手机APP。

![image-20250916135443389](README_assets/image-20250916135443389.png)

打开软件，点击“进阶套件”-“TonyPi”-“Tony Pi Pro”

![image-20250916142806700](README_assets/image-20250916142806700.png)

点击右下角加号，选择直连模式，连接HW开头的热点，密码为hiwonder。

![image-20250916142937592](README_assets/image-20250916142937592.png)

![image-20250916143024979](README_assets/image-20250916143024979.png)

![image-20250916143216510](README_assets/image-20250916143216510.png)

连接完成后返回APP，再次搜索设备可看见可用设备：

![image-20250916143326463](README_assets/image-20250916143326463.png)

长按设备可查看ip和id：

![image-20250916143421266](README_assets/image-20250916143421266.png)

点击设备，进行操作。

![image-20250916143445118](README_assets/image-20250916143445118.png)





#### 连接到局域网

> 机器人成功连接到局域网之后就不会再开启HW开头的热点，要再次开启热点，根据[重启热点](#重启热点)进行操作。

手机先连接到HW开头的热点，打开app，选择局域网模式。

![image-20250916151723106](README_assets/image-20250916151723106.png)

选择wifi（wifi名称为英文）进行连接

![image-20250916152637567](README_assets/image-20250916152637567.png)

输入wifi密码，等待连接完成。

![image-20250916152713830](README_assets/image-20250916152713830.png)

![image-20250916152729409](README_assets/image-20250916152729409.png)

连接完成后，手机连接到wifi，选择局域网模式

![image-20250916152942481](README_assets/image-20250916152942481.png)

![image-20250916152954183](README_assets/image-20250916152954183.png)

从该页面返回

![image-20250916151847673](README_assets/image-20250916151847673.png)

刷新，出现设备，即进入到局域网模式，长按可查看ip和id。

 ![image-20250916153135373](README_assets/image-20250916153135373.png)

![image-20250916153232124](README_assets/image-20250916153232124.png)



### 重启热点

#### 拆下机器人后盖

> 仅需要重启热点，也可以不拆下机器人后盖，可以直接按到K1。

在关机状态下，分别拧下机器人后盖左右两侧共4颗螺丝。

![image-20250916154144411](README_assets/image-20250916154144411.png)

![image-20250916154211048](README_assets/image-20250916154211048.png)

拆下后盖之后，开机，等待机器人完成启动。可看见主板上的K1按钮、LED灯：

![image-20250916154448672](README_assets/image-20250916154448672.png)

![image-20250916155235378](README_assets/image-20250916155235378.png)

长按K1，直到LED2由常亮变成闪烁，机器人切换为直连模式，重新开启HW开头的热点。





## 开发环境准备

参考[软件环境安装文档](./docs/01_dev_env.md)中[python安装](./docs/01_dev_env.md/#python安装)与[VSCode安装](./docs/01_dev_env.md/#VSCode安装)。

打开vscode，在插件中搜索remote，下载Remote-SSH。

![image-20250917111007435](README_assets/image-20250917111007435.png)

下载完成，左侧工具栏会有远程连接图标，点击打开，点击加号，新建远程。

![image-20250917111230221](README_assets/image-20250917111230221.png)

在输入框中输入ssh连接命令，选择一个配置，SSH中会显示新的连接。

```shell
ssh 用户名@ip
```

![image-20250917111344412](README_assets/image-20250917111344412.png)

![image-20250917111630395](README_assets/image-20250917111630395.png)

![image-20250917111720167](README_assets/image-20250917111720167.png)

点击设置，打开ssh配置文件，可以看见所有的ssh连接配置。

![image-20250917111902040](README_assets/image-20250917111902040.png)

点击ip右侧的按钮，开启远程连接。

![image-20250917112016444](README_assets/image-20250917112016444.png)

初次连接，远程主机会下载vscode服务器，连接完成后如下图：

![image-20250917112110744](README_assets/image-20250917112110744.png)

点击文件夹，选择打开文件夹/home/pi

![image-20250919102559348](README_assets/image-20250919102559348.png)

![image-20250919102627829](README_assets/image-20250919102627829.png)





## 练习

+ 完成机器人远程桌面连接、手机app连接以及直连模式与局域网模式的切换

+ 完成[软件环境安装文档](./docs/01_dev_env.md)中其它软件的安装
+ 提出三个任何与本节内容相关的问题，并自行回答



# Python与机器人基本控制（第2周）

### 打印输出与注释

```python
"""
TonyPiPro基于树莓派5B开发，它在TonyPi机器人的基础上做了很多升级，使
得TonyPi
Pro不仅保留了之前所有的功能，还拓展出了更多有趣的AI创意玩
法，如跨栏越障、上下台阶、智能抓取、口罩识别、多台群控等等。它不仅能
满足用户对机器视觉、机器人运动学等算法的学习和验证，还为传感器应用、
视觉抓取等二次开发提供快速、便捷的集成方案。
"""

print("欢迎来到人形机器人实验室！")
print("今天的主角是"+" TonyPi"+" 机器人")

```





### python数据类型

#### 基本类型

```python
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

```



#### 容器与遍历

```python
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

```



#### 类型转换与基本运算符

```python
# 类型转换：把整型转成字符串
degree_of_freedom = 8
degree_of_freedom_str = str(degree_of_freedom)
print("机器人有 " + degree_of_freedom_str + " 个自由度")

# 基本运算符：计算机器人运动总时长
frequency = 4  # 重复4次
walk_time = 5  # 前进 5 秒
back_time = 3  # 后退 3 秒
v_m_per_s = 0.3 #速度
print(f"机器人运行{(walk_time+back_time)*frequency}秒，"
      f"前进{(walk_time-back_time)*frequency*v_m_per_s}米，"
      f"平均前进速度为{((walk_time-back_time)*frequency*v_m_per_s)/((walk_time+back_time)*frequency)}米/秒")

```



### 流程控制

#### if条件判断

```python
robot_battery_level = 25  # 电池电量百分比

if robot_battery_level < 20:
    print("⚠️ 电量不足，请及时充电！")
else:
    print("✅ 电量充足，可以继续运行")

```



#### for/while循环

```python
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

```



#### 嵌套循环与break/continue

```python
# 模拟机器人在两层楼中巡逻
floors = [1, 2]
rooms = ["101", "102", "103"]

for f in floors:
    for r in rooms:
        if r == "102" and f == 2:
            print("遇到障碍物，跳过房间", r)
            continue
        if r == "103" and f == 2:
            print("紧急任务，结束巡逻！")
            break
        print(f"机器人正在巡逻 {f} 楼 {r} 房间")

```



### 函数与模块

#### 函数定义与调用

```python
def robot_say(message):
    print("🤖 机器人:", message)

# 调用函数
robot_say("你好！我是 TonyPi")

```



#### 传入参数与返回值

```python
def move_forward(steps):
    print(f"机器人前进 {steps} 步")
    return steps * 0.3  # 每步 0.3 米，返回总距离

distance = move_forward(10)
print("机器人总共移动了", distance, "米")

```



### python内置模块导入

```python
import time

print("机器人启动中...")
time.sleep(2)  # 延时 2 秒
print("启动完成 ✅")

```



### 类与面向对象基础

> 面向对象就是**把现实世界的事物抽象成对象，用对象的属性（数据）和方法（行为）来组织和管理程序**

#### 类的定义与实例化

定义一个Robot类，定义实例化方法。

```python
class Robot:
    def __init__(self, name, servo_count):
        self.name = name
        self.servo_count = servo_count

# 创建机器人对象
robot = Robot("TonyPi", 20)
print("机器人名称:", robot.name)
print("舵机数量:", robot.servo_count)

```



#### 属性与方法

```python
class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery  # 电池电量

    def speak(self, msg):
        print(f"{self.name} 说:", msg)

    def charge(self, amount):
        self.battery += amount
        print(f"{self.name} 已充电，现在电量 {self.battery}%")

# 使用类
robot = Robot("TonyPi", 50)
robot.speak("大家好，我是TonyPi！")
robot.charge(30)

```



### python控制机器人基本运动

水平行走、抓握、转头等。



## 练习

+ 利用AI，自行了解容器：
  + 增删改查
  + 列表：切片、列表推导式、解包等
  + 字典：字典推导式、合并字典、解包等
  + 元组：切片、解包、嵌套元组等

+ 以面向对象的思想，加上机器人的基本控制，设计一个机器人的功能模块
+ 提出三个任何与本节内容相关的问题，并自行回答





# OpenCV与机器人视觉（第3周）

## 打开机器人摄像头

实时获取机器人看到的画面。

## 图像预处理

灰度化：减少计算量

模糊：去除噪声

边缘检测：用于检测地面边界、障碍物

## 绘制图形

绘制检测框

## 形状与轮廓检测

检测地上的物体（比如足球、障碍物）

## 颜色识别

让机器人识别红色球 → 追球运动

颜色标签识别

## 人脸检测

机器人识别人类，做互动（比如挥手、打招呼）。

## 目标跟踪

机器人锁定目标位置 → 头部/身体转向



## 练习

+ 使用本节内容设计一个与机器人视觉相关的功能模块
+ 提出三个任何与本节内容相关的问题，并自行回答



# 机器人语音识别与语音合成（第4周）

## 语音模块安装与接线

## 语音控制TonyPi

## 颜色识别与播报

## 语音API

## 开源项目介绍

### Index-TTS(TTS)

### sherpa-onnx(ASR)

## 练习

+ 结合本节依旧之前所学内容，设计一个语音相关的功能模块
+ （可选）使用Index-TTS与sherpa-onnx替代机器人原本的语音模块进行交互
+ 提出三个任何与本节内容相关的问题，并自行回答



# 机器人传感器（第5周）

## 风扇模块实验

## 触摸传感器实验

## MP3模块实验

## 超声波传感器实验

## 点阵模块实验

## 光线传感器实验

## 练习

+ 结合本节以及之前所学内容，设计一个传感器相关的功能模块
+ 提出三个任何与本节内容相关的问题，并自行回答

# 机器人AI模块（第6周）

## YOLO目标检测

模型部署、训练

## LLM大语言模型

基本概念、原理、主流模型调用

## MCP Server与Client

编写MCP服务端与客户端，让大模型能调用自定义的工具。



## 练习

+ 结合本节以及之前所学内容，设计一个大模型+MCP的功能模块
+ 提出三个任何与本节内容相关的问题，并自行回答



# 智能搬运与田径跨栏（第7周）

## 智能巡线

## 道具安装以及地图的铺设

## 爬台阶

## 跨栏运动

## 田径运动

## 练习

+ 使用机器人完成本节内容
+ 提出三个任何与本节内容相关的问题，并自行回答



# 大模型与机器人整合（第8周）

## 系统设计

## 示例项目：语音/手势控制

根据语音与手势与机器人进行交互。

## 练习

+ 完成一个大模型与机器人整合的系统设计
+ 提出三个任何与本节内容相关的问题，并自行回答

# 综合实践（第9-10周）

方案一：田径跨栏+物品搬运。

方案二：自主设计一个作品（包含机器人运动、视觉、语音、大模型）。

## 练习

+ 选择一个方案完成作为结课大作业

# 作品展示（第11周）

同学展示作品。







# temp

## 机器上部署web应用

Flask 是一个轻量级的web "微框架"，非常适合在树莓派这样的设备上运行。

安装Flask和gunicorn

```shell
pip install flask
pip install gunicorn
```

创建app.py文件，编写：

```python
from flask import Flask, jsonify 
import hiwonder.ActionGroupControl as AGC

# 初始化Flask应用
app = Flask(__name__)

# 创建一个API端点来执行动作
# 可以通过访问 http://<树莓派IP>:5000/run_action/stand 来让机器人站立
@app.route('/run_action/<string:action_name>', methods=['GET'])
def run_robot_action(action_name):
    try:
        print(f"接收到指令，执行动作: {action_name}")
        # 直接调用您SDK中的函数
        # 注意：这里的路径需要是机器人的实际路径，如果SDK默认值正确则无需修改
        AGC.runAction(action_name)
        return jsonify({"status": "success", "action": action_name})
    except Exception as e:
        print(f"执行动作失败: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # 监听所有网络接口，这样局域网内的设备才能访问
    app.run(host='0.0.0.0', port=5000)
```



启动app：

```shell
gunicorn --workers 2 --bind 0.0.0.0:5000 app:app
```



+ --workers 2: 指定了2个工作进程来处理请求，提高了并发能力。对于树莓派5，2到4个工作进程是合理的。
+ --bind 0.0.0.0:5000: 和 app.run() 中的 host 和 port 作用一样，监听所有网络接口的5000端口。
+ app:app: 第一个 app 指的是python文件名 `app.py`，第二个 app 指的是在该文件中创建的 Flask 实例 `app = Flask(__name__)`。

启动后终端输出：

```shell
❯ gunicorn --worker-class gevent --workers 2 --bind 0.0.0.0:5000 app:app
/home/pi/.local/lib/python3.11/site-packages/zope/__init__.py:3: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
[2025-09-18 13:51:45 +0800] [4589] [INFO] Starting gunicorn 23.0.0
[2025-09-18 13:51:45 +0800] [4589] [INFO] Listening at: http://0.0.0.0:5000 (4589)
[2025-09-18 13:51:45 +0800] [4589] [INFO] Using worker: gevent
[2025-09-18 13:51:45 +0800] [4590] [INFO] Booting worker with pid: 4590
[2025-09-18 13:51:45 +0800] [4591] [INFO] Booting worker with pid: 4591
[2025-09-18 13:51:49 +0800] [4589] [INFO] Handling signal: winch

```

打开浏览器输入：

```shell
http:机器人ip:5000/
```

正常返回json数据，说明启动正常。

![image-20250919112329405](README_assets/image-20250919112329405.png)







# 预设动作



| 动作名称                   | 动作内容         | 说明 |
| -------------------------- | ---------------- | -------------------------- |
| 0                          | 伸展手臂         |  |
| 16                         | 机械舞1          |  |
| 17                         | 机械舞2          |  |
| 18                         | 机械舞3          |  |
| 19                         | 机械舞4          |  |
| 20                         | 机械舞5          |  |
| 21                         | 机械舞6          |  |
| 22                         | 机械舞7          |  |
| 23                         | 机械舞8          |  |
| 24                         | 机械舞9          |  |
| back_end                   | -                |  |
| back_fast                  | 向后移动         |  |
| back_one_step              | 向后移动一步     |  |
| back_start                 | -                |  |
| back                       | 小幅向后移动一步 |  |
| bow                        | 鞠躬             |  |
| catch_ball_0               | 抱球             |  |
| catch_ball_go_slow         | 抱球向前走       |  |
| catch_ball_go_up           | 举球向前走       |  |
| catch_ball_left_move       | 抱球向左移动     |  |
| catch_ball_left_move_up    | 举球向左移动     |  |
| catch_ball_right_move      | 抱球向右移动     |  |
| catch_ball_right_move_up   | 举球向右移动     |  |
| catch_ball_turn_left_up    | 举球左转         |  |
| catch_ball_turn_left       | 抱球左转         |  |
| catch_ball_turn_right_up   | 举球右转         |  |
| catch_ball_turn_right      | 抱球右转         |  |
| catch_ball_up              | 蹲下抱球举起     |  |
| catch_ball                 | 蹲下抱球站起     |  |
| chest                      | 向后弯腰，捶胸   |  |
| climb_stairs_1             | 爬台阶           |  |
| climb_stairs               | 爬台阶           |  |
| creep_forward              | 向前爬           |  |
| down_floor_1               | -                |  |
| down_floor                 | 下台阶           |  |
| down_objec                 | 蹲下 |  |
| go_forward_end             | - |  |
| go_forward_fast            | 快速向前走 |  |
| go_forward_one_small_step | 向前移动一小步 |  |
| go_forward_one_step        | 向前走一步 |  |
| go_forward_start_fast      | 快速向前走一步 |  |
| go_forward_start           | 快速向前走一步 |  |
| go_forward                 | 向前走（走偏） |  |
| go_hand_up                 | 左手举在胸前，向前走（走偏） |  |
| go_hand_up1                | 左手举在胸前，向前走 |  |
| go                         | 双手举到头顶，向前走 |  |
| grab_left                  | 蹲下双臂张开，左手往胸前收 |  |
| grab_right                 | 蹲下双臂张开，右手往胸前收 |  |
| grab_squat_left            | 蹲下，左手放置胸前 |  |
| grab_squat_right           | 蹲下，右手放置胸前 |  |
| grab_squat_up_left         | 蹲下起立，抬起左手 |  |
| grab_squat_up_right        | 蹲下起立，抬起右手 |  |
| grab_stand_left            | 抬起左手，伸展，放下 |  |
| grab_stand_right           | 抬起右手，伸展，放下 |  |
| huibi                      | 抬起左手，放下 |  |
| hurdles                    | 跨栏 |  |
| left_hand                  | 小幅度抬起左手 |  |
| left_kick                  | 向右倾，抬起左脚 |  |
| left_move_10               | 向左移动小步 |  |
| left_move_20               | 向左移动小步 |  |
| left_move_30               | 向左移动小步 |  |
| left_move_40               | 向左移动 |  |
| left_move_fast             | 快速向左移动一步 |  |
| left_move                  | 向左移动一步 |  |
| left_shot_fast             | 向右倾，左踢腿 |  |
| left_shot                  | 向右倾，左踢腿 |  |
| left_uppercut              | 抬右手，伸展左手 |  |
| lie_down                   | 躺下 |  |
| lift_down                  | 左手抬到胸前，放下 |  |
| lift_left_hand             | 左手抬到胸前 |  |
| lift_up                    | 缓慢左手抬到胸前 |  |
| move_up                    | 蹲下，抱球，站起，将手举到头顶 | put_up_object恢复站立 |
| put_down_object            | 蹲下，身体前倾，伸出右手 |  |
| put_down                   | 蹲下，抱球举起，放下 |  |
| put_down2                  | 将举到头顶的手放下 |  |
| put_down3                  | 蹲下，抱球，放开，站起 |  |
| put_up_object              | 从put_down_object恢复到站立 |  |
| right_hand                 | 小幅抬起右手，放下 |  |
| right_kick                 | 身体左倾，抬起右脚，恢复站立 |  |
| right_move_10              | 向右移动一小步 |  |
| right_move_20              | 向右移动一小步 |  |
| right_move_30              | 向右移动一小步 |  |
| right_move_40              | 向右移动一小步 |  |
| right_move_fast            | 快速向右移动一步 |  |
| right_move                 | 向右移动一步 |  |
| right_shot_fast            | 身体左倾，右踢腿 |  |
| right_shot                 | 身体左倾，右踢腿 |  |
| right_uppercut             | 右手抬到胸前，举举起左手 |  |
| right                      | 在双手举到头顶状态下，右转 |  |
| seize_down_right           | 右手抬到胸前，放下 |  |
| seize_right                | 右手抬到胸前 |                       |
| sit_ups                    | 仰卧起坐 |  |
| squat_down                 | 伸展双臂，蹲下，手臂环抱 |  |
| squat_up                   | 蹲下，抬起手臂环抱，站起，伸展手臂，放下 |  |
| squat                      | 蹲下，手臂环抱 |  |
| stand_slow                 | 站起 |  |
| stand_up_back              | 从躺地状态，站起 |  |
| stand_up_front             | 从趴地状态，站起 |  |
| stand | 站起 |  |
| stepping | 原地小踏步 |  |
| temp1 | 向后走一步 |  |
| toulan_0 | 双手举起，稍微向下放张开 |  |
| toulan_a | 双手举到头顶前 |  |
| toulan_b | 双手举起，稍微向下放张开 |  |
| turn_left_fast | 向左转 |  |
| turn_left_small_step_a | 缓慢向左转 |  |
| turn_left_small_step | 缓慢向左转 |  |
| turn_left | 向左转 |  |
| turn_right_fast | 向右转 |  |
| turn_rifht_small_step_a | 缓慢向右转 |  |
| turn_rifht_small_step | 缓慢向右转 |  |
| turn_right | 向右转 |  |
| twist | 伸展双手，身体左右扭 |  |
| wave | 抬起右手，摆手 |  |
| wing_chun | 双手抬到胸前，上下摆臂 |  |





