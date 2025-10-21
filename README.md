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
我们将从人形机器人的发展简史、应用场景及基本技术讲起，并完成TonyPi Pro机器人的开发环境准备工作。

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

+ 掌握人形机器人的基本原理；

+ 独立完成基于Python的机器人程序设计；

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

#### 开机

将机器人背面底部的树莓派扩展板开关由“**OFF**”推动到“**ON**”，设备开机成功后，蜂鸣器会“嘀”的一声，此时扩展板的LED1、LED2以及树莓派的指示灯都将常亮。

![image-20250916110921218](README_assets/image-20250916110921218.png)

![image-20250916110952446](README_assets/image-20250916110952446.png)

![image-20250924111158921](README_assets/image-20250924111158921.png)



#### 关机

> 关机**不要直接关掉电源开关**，否则再次开机可能出现LED2灯不亮，即网络连接异常。

线连接到机器人，打开终端，输入命令将树莓派先关机：

**立刻关机**

```shell
sudo shutdown -h now
```

**延时关机**(30分钟后关机)

```shell
sudo shutdown -h 30
```

树莓派关机后，树莓派的指示灯为红灯，扩展版上的LED2灯是灭的，然后再将电源开关关掉。

![image-20250924110415387](README_assets/image-20250924110415387.png)









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

从该页面返回。

![image-20250916151847673](README_assets/image-20250916151847673.png)

刷新，出现设备，即进入到局域网模式，长按可查看ip和id。

 ![image-20250916153135373](README_assets/image-20250916153135373.png)

![image-20250916153232124](README_assets/image-20250916153232124.png)



#### 网线连接机器人

以windows系统为例演示。

##### 网线连接电脑与机器人

拆开机器人后盖，可以在机器人右侧看见一个网口，将网线连接即可。

![image-20250925100455942](README_assets/image-20250925100455942.png)





##### 配置网络共享

先让电脑连接到一个网络，这个网络不占用网口，比如无线网络WLAN。

按下WIN搜索“控制面板”，或者WIN+R输入control，打开控制面板。

点击“网络和Internet”——“网络和共享中心”——“更改适配器设置”，可以看到两个网路适配器：

+ 连接的WLAN，也就是WIFI
+ 连接的机器人

选中WLAN适配器，鼠标单击右键，点击“属性”——“共享”，两个选项都勾选，选择机器人连接的网络适配器，点击确认。

共享之后，可以看见WLAN会提示“共享的”。

![share_net](README_assets/share_net.png)



##### 共享失败

Windows网络共享后，使用共享网络的适配器（也就是连接机器人的网络适配器）ip会变为`192.168.137.1`。需要检查是否有其它网络适配器占用了这个ip。

选择网络适配器，右键单击鼠标，点击“Internet协议版本4（TCP/IPv4）”，即可查看当前适配器的ip，如果被占用了，需要将ip改为其它非`192.168.137.1`的ip地址。

![image-20250925110629505](README_assets/image-20250925110629505.png)

![image-20250925110322010](README_assets/image-20250925110322010.png)



##### 查找机器人ip

打开电脑命令行终端，输入：

```shell
arp -a
```



可以看到一系列接口：

```shell
C:\Users\lsn>arp -a

接口: 192.168.5.1 --- 0xe
  Internet 地址         物理地址              类型
  192.168.5.255         ff-ff-ff-ff-ff-ff     静态
  224.0.0.2             01-00-5e-00-00-02     静态
  224.0.0.22            01-00-5e-00-00-16     静态
  224.0.0.251           01-00-5e-00-00-fb     静态
  224.0.0.252           01-00-5e-00-00-fc     静态
  224.0.1.129           01-00-5e-00-01-81     静态
  239.255.255.250       01-00-5e-7f-ff-fa     静态
  255.255.255.255       ff-ff-ff-ff-ff-ff     静态

接口: 192.168.123.1 --- 0x12
  Internet 地址         物理地址              类型
  192.168.123.255       ff-ff-ff-ff-ff-ff     静态
  224.0.0.2             01-00-5e-00-00-02     静态
  224.0.0.22            01-00-5e-00-00-16     静态
  224.0.0.251           01-00-5e-00-00-fb     静态
  224.0.0.252           01-00-5e-00-00-fc     静态
  224.0.1.129           01-00-5e-00-01-81     静态
  239.255.255.250       01-00-5e-7f-ff-fa     静态
  255.255.255.255       ff-ff-ff-ff-ff-ff     静态
  ...
```



找到`192.168.137.1`开头的接口，第一个192.168.137开头的ip，也就是`192.168.137.95`为机器人ip。

![image-20250925111132310](README_assets/image-20250925111132310.png)

命令行终端输入：

```shell
ssh pi@192.168.137.95
```

然后输入密码`raspberrypi`，即可远程登录。

```shell
C:\Users\lsn>ssh pi@192.168.137.95
pi@192.168.137.95's password:
Linux raspberrypi 6.6.74+rpt-rpi-2712 #1 SMP PREEMPT Debian 1:6.6.74-1+rpt1 (2025-01-27) aarch64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Sep 25 12:33:05 2025
|MACHINE|MIC_TYPE|: |TonyPi|WonderEchoPro|
ASR_LANGUAGE: Chinese
VERSION: |V1.0|2025-04-21|
zsh: corrupt history file /home/pi/.zsh/.zsh_history
╭─  │  ~                                                                  ✔ │ base  │ pi@raspberrypi │ 12:41:42 
╰─
```





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



## 镜像烧录

### 软件安装

#### Raspberry Pi Imager

在官网，[Raspberry Pi software – Raspberry Pi](https://www.raspberrypi.com/software/)，下载安装树莓派镜像烧录器。主要用来初始化SD卡，让树莓派能够从SD启动。官网只能下载基本镜像，机器人的镜像是要其它软件进行烧录。

![image-20251008160913151](README_assets/image-20251008160913151.png)



#### SD CARD FORMATTER

用于格式化SD卡，在[官网](https://www.sdcardformatter.com/)下载安装即可。

![image-20251008161548031](README_assets/image-20251008161548031.png)



#### Win32 Disk Imager

用于烧录机器人的镜像，在[Win32 Disk Imager官网](https://sourceforge.net/projects/win32diskimager/)，下载后安装即可。

![image-20251008161254454](README_assets/image-20251008161254454.png)







### 初始化SD卡

拆开机器人的后盖，将SD取下，插到读卡器中。

![image-20251009125322786](README_assets/image-20251009125322786.png)

初始化SD卡：

+ 1-2：打开树莓派烧录工具，点击“选择SD卡”，选择插入的SD卡。
+ 3：选择 SD 卡后，点击选择操作系统。
+ 4：拉到下面选择 Format card as FAT32，对 SD 卡进行格式化。
+ 5-6：点击 NEXT 和是进行格式化。（格式化成功后会有以下提示并且接着点击继续）。
+ 7：再次点击选择 SD 卡和选择写入的操作系统。
+ 8-10：在写入的操作系统选项拉到下面选择 Misc utility images，选择 Bootloader(Pi 5 family)，再次选择 SD Card Boot。
+ 11：点击 NEXT 和是。
+ 12：完成后点击继续。

![烧录](README_assets/烧录-175991207869612.png)



然后**将烧好固件的 SD 卡插入树莓派5**，并且打开电源。至少等待 10 秒到 20 秒的时间。如果成功，树莓派的 act 灯会永远快速闪烁。更新修复完成后，将 SD 卡移出来。

![image-20251008163423410](README_assets/image-20251008163423410.png)



### 格式化SD卡

打开SD Card Formatter，将“**Select card**”一栏选择为SD卡的盘符，并点击“**Format**”，将SD卡格式化。

![image-20251008163554428](README_assets/image-20251008163554428.png)

 若出现下图所示提示，点击“**是**”按键即可。等待格式化完成。

![image-20251008163610015](README_assets/image-20251008163610015.png)



### 镜像烧录

打开镜像烧录工具（Win32DiskImager），选择镜像文件。**镜像文件的存放路径不能存在中文字符。**

![image-20251008163717606](README_assets/image-20251008163717606.png)

若出现下图所示提示，点击“Yes”按键即可。

![image-20251008163931418](README_assets/image-20251008163931418.png)



若提示“Write Successful”，则烧录成功。若出现报错，请关闭防火墙一类的软件，并重新插入SD卡，再次进行本节操作。

![image-20251008164001227](README_assets/image-20251008164001227.png)



烧录完成后将 SD卡弹出，从读卡器中拔下来，插入到树莓派主板上开机启动即可。



## 练习

+ 完成本节课与机器人有关的操作。

+ 完成[软件环境安装文档](./docs/01_dev_env.md)中其它软件的安装
+ 提出三个任何与本节内容相关的问题，并自行回答



# Python与机器人基本控制（第2周）

## 打印输出与注释

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





## python数据类型

### 基本类型

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



### 容器与遍历

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



### 类型转换与基本运算符

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



## 流程控制

### if条件判断

```python
robot_battery_level = 25  # 电池电量百分比

if robot_battery_level < 20:
    print("⚠️ 电量不足，请及时充电！")
else:
    print("✅ 电量充足，可以继续运行")

```



### for/while循环

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



### 嵌套循环与break/continue

```python
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

```



## 函数与模块



### 函数定义与调用

```python
def robot_say(message):
    print("🤖 机器人:", message)

# 调用函数
robot_say("你好！我是 TonyPi")

```



### 传入参数与返回值

```python
def move_forward(steps):
    print(f"机器人前进 {steps} 步")
    return steps * 0.3  # 每步 0.3 米，返回总距离

distance = move_forward(10)
print("机器人总共移动了", distance, "米")

```



## 模块导入

```python
# python内置模块
import logging

# 第三方模块
from flask import Flask, jsonify, request

# 自定义模块
from src.utils.resp import CanStartResult

```





## 安装第三方库

使用pip命令可以安装第三方的依赖库：

```shell
pip install 包名
```

执行命令之后pip会下载对应的包，不过官方的下载源处于国外，所以下载可能会因为网络问题而失败。这个时候可以使用`-i`参数添加国内的镜像源，来加速下载。

下面使用清华源下载了flask：

```shell
pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple
```



**常用镜像源**

```shell
# 清华源
https://pypi.tuna.tsinghua.edu.cn/simple

# 上交大
https://mirror.sjtu.edu.cn/pypi/web/simple/
```





## 类与面向对象基础

> 面向对象就是**把现实世界的事物抽象成对象，用对象的属性（数据）和方法（行为）来组织和管理程序**

### 类的定义与实例化

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



### 属性与方法

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



## python控制机器人基本运动



### 创建虚拟环境

使用conda创建虚拟环境，激活。进入`/home/pi/TonyPi/HiwonderSDK`路径。

赋予执行权限：

```shell
chmod +x /home/pi/TonyPi/HiwonderSDK
```

安装完成：

```shell
Successfully built hiwonder
Installing collected packages: hiwonder
Successfully installed hiwonder-1.0
```

安装pyserial

```shell
pip install pyserial -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```



创建文件夹：

```shell
mkdir /home/pi/src
```



创建一个test01.py文件，编写：

```python
import hiwonder.ActionGroupControl as AGC
AGC.runActionGroup('go_forward_one_step')  
```

运行程序：

```shell
python test01.py
```

如果依赖安装成功，运行时机器人会向前移动。



### 直接在机器人上执行

使用vscode连接到机器人：

![image-20250922154833442](README_assets/image-20250922154833442.png)





#### 行走

TonyPi机器人采用动作文件来管理机器人的肢体动作执行。在`/home/pi/TonyPi/ActionGroups`路径下可以看到预设的动作，简要描述信息可查看[预设动作](#预设动作)。我们通过调用动作文件让机器人执行动作，从而控制机器人。

![image-20250923130533667](README_assets/image-20250923130533667.png)



**向前走**

```python
import hiwonder.ActionGroupControl as AGC

AGC.runActionGroup('go_forward_one_step', times=2, with_stand=True)                         
# 第二个参数为运行动作次数，默认1, 当为0时表示循环运行， 第三个参数表示最后是否以立正姿态收步

```



**停止运行**

```python
threading.Thread(target=AGC.runActionGroup, args=('go_forward', 0, True)).start()  
# 运行动作函数是阻塞式的，如果要循环运行一段时间后停止，请用线程来开启
time.sleep(3)
AGC.stopActionGroup()  # 前进3秒后停止
```





**向后走**

```python
import hiwonder.ActionGroupControl as AGC


AGC.runActionGroup('back_one_step')
```



**向左走**

```python
import hiwonder.ActionGroupControl as AGC


AGC.runActionGroup('left_move')
```



**向右走**

```python
import hiwonder.ActionGroupControl as AGC


AGC.runActionGroup('right_move')
```







#### 转头

> 上下转动的舵机限制角度在130°左右，左右180°，范围在500-2500之间。


```python
import hiwonder.ros_robot_controller_sdk as rrc
from hiwonder.Controller import Controller


board = rrc.Board()
ctl = Controller(board)

ctl.set_pwm_servo_pulse(1, 1700, 500) # 上下转头
ctl.set_pwm_servo_pulse(2, 1400, 500) # 左右转头
```

三个参数：

+ servo_id: 要驱动的舵机id(the servo id needed to be driven)

+ pulse:   舵机目标位置(servo target position)

+ use_time: 转动需要的时间(the time needed to rotate)



### 在电脑上远程控制机器人

由于Tonypi机器人的SDK是直接控制舵机，将SDK安装到电脑上是无法正常使用的，因此我们使用web框架在机器人上创建一个web应用，通过web应用间距控制机器人。



#### 安装Flask

Flask 是一个轻量级的web "微框架"，非常适合在树莓派这样的设备上运行。

安装Flask和gunicorn：

```shell
pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple
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
gunicorn --workers 4 --timeout 600 --bind 0.0.0.0:5000 app:app
```



+ --workers 2: 指定了2个工作进程来处理请求，提高了并发能力。对于树莓派5，2到4个工作进程是合理的。
+ --timeout 600：设置超时时间，600s。
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



#### 控制运动

浏览器输入：

```shell
http://机器人IP:5000/run_action/go_forward_one_step
```

可以看到机器人执行了动作，向前走了一步。以此类推，可以执行其它动作。



#### 控制转头

添加控制转头的代码，启动程序。

```python
from flask import Flask, jsonify, request
import hiwonder.ActionGroupControl as AGC
import hiwonder.ros_robot_controller_sdk as rrc
from hiwonder.Controller import Controller

# 初始化Flask应用
app = Flask(__name__)
board = rrc.Board()
ctl = Controller(board)


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


@app.route('/turn_head', methods=['POST'])
def turn_head():
    req_data = request.get_json()
    servo_id = req_data.get('servo_id')
    pulse = req_data.get('pulse')
    ctl.set_pwm_servo_pulse(servo_id, pulse, 500)
    return jsonify({"status": "success", "servo_id": servo_id, "pulse": pulse})


if __name__ == '__main__':
    # 监听所有网络接口，这样局域网内的设备才能访问
    app.run(host='0.0.0.0', port=5000)
```

控制转头的程序使用POST请求举例，不过浏览器不能直接发送POST请求，所以可以使用cmd终端或者[http请求调试工具](./docs/01_dev_env.md#http请求调试工具)，这里以Apifox为例：

![image-20250923154112592](README_assets/image-20250923154112592.png)



## 编辑动作

使用VNC连接到机器人，在桌面可以看到一个名为Tonypi的软件，点击打开。

![image-20251010165913063](README_assets/image-20251010165913063.png)

点击Execute。

![image-20251010165936515](README_assets/image-20251010165936515.png)

打开后可以看到机器人动作编辑界面。

![image-20251010170015632](README_assets/image-20251010170015632.png)



### 设置舵机位置

我们可以在界面上通过拖拽条来设置舵机的参数，拖拽的时候舵机位置会同步改变。

此外，也可以点击“手掰编程”，然后直接掰动机器人关节，来设置舵机的位置。

![image-20251010170437181](README_assets/image-20251010170437181.png)



### 角度回读

设置完舵机位置之后，点击“角度回读”，舵机参数会显示在右侧的列表中。

![image-20251010170926368](README_assets/image-20251010170926368.png)



### 执行动作

点击列表中动作后选中该动作，然后点击左侧的启动按钮，机器人舵机的位置就会设置成这个动作对应的舵机位置。

![image-20251010171243442](README_assets/image-20251010171243442.png)



点击“运行”按钮，可以顺序执行所有的动作。

![image-20251010171355184](README_assets/image-20251010171355184.png)



### 删除动作

点击选中动作后，点击“删除动作”按钮，可以删除这个动作。

![image-20251010171458633](README_assets/image-20251010171458633.png)

![image-20251010171508927](README_assets/image-20251010171508927.png)



### 保存动作

点击“保存动作文件”，输入文件名称，点击Save，当前所有动作就会被保存为一个.d6a格式的二进制文件。

保存的路径可以任意，不过一般保存在`/home/pi/TonyPi/ActionGroups`，这个路径是预设动作的保存路径。

![image-20251010171707930](README_assets/image-20251010171707930.png)



### 打开动作文件

点击“打开动作文件”，选择`/home/pi/TonyPi/ActionGroups`路径，可以选择需要执行的动作文件。动作文件的行为动作，可以查看附录下的[动作预设](#预设动作)。

![image-20251010172309654](README_assets/image-20251010172309654.png)



打开动作文件后，右侧列表会展示所有动作，点击“运行”，即可运行这个动作文件。

![image-20251010172355878](README_assets/image-20251010172355878.png)



## 多线程与继承

**线程**是操作系统调度的最小执行单元。**多线程**就是在同一个进程中运行多个线程，可以同时执行不同任务。在 Python 中，使用 `threading` 模块来实现。



### 基本线程创建

```python
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

```

执行程序，可以看到，机器人一边向前走，一边转头。



### 使用类继承

当功能需求较复杂时，可以继承Thread类来进行实现。以下情况可以考虑使用类继承：

+ 需要在线程对象里保存状态、返回值或异常。

+ 需要封装一个“长期运行”的工作线程（比如消费者/监听器），并提供 start/stop 等方法。

+ 需要在 run 里加统一的前后处理（日志、计时、资源初始化/清理）。

+ 需要把线程作为更大类层次的一部分，复用面向对象接口。



下面是一个启动（停止）机器人向前行走的例子：

`src/w02/thread_control.py`

```python
import threading
import time
import hiwonder.ActionGroupControl as AGC

class WalkController(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self._run_event = threading.Event()
        self._run_event.set()
        self._stop_event = threading.Event()
        
    def run(self):
        while not self._stop_event.is_set():
            if self._run_event.wait():
                AGC.runActionGroup('go_forward_one_step')
            
    def pause(self):
        self._run_event.clear()
        AGC.stopActionGroup()

    def resume(self):
        self._run_event.set()

    def stop(self):
        self._stop_event.set()
        self._run_event.set()


if __name__ == "__main__":
    walk_controller = WalkController("WalkController")
    walk_controller.start()
    time.sleep(3)  
    walk_controller.pause()
    time.sleep(2)  
    walk_controller.resume()
    time.sleep(3)  
    walk_controller.stop()

```

运行程序，可以看到机器人向前行走3秒后，暂停2秒，然后再次行走3秒后结束。

> 上面的例子已经可以实现机器人的启动、暂停、停止。但是有一个问题：这个实例只能执行一次，一旦停止，就没法再次启动了。



### 实现可重复启停的机器人控制器

#### `robot_action.py`

src/w02/robot_action.py

这个文件中有一个`Action`类，这个类是机器人动作控制器的父类

##### 类定义

**属性**

---

`_status: ActionStatus`：用于标明action的运行状态，类型为枚举类型ActionStatus。

`_thread: Optional[threading.Thread]`：执行动作的线程。

`_run_event: threading.Event`：运行标志，用于标明线程是否在运行。

`_stop_event: threading.Event`：停止标志，用于标明线程是否停止。

`_lock`：锁，保证并发安全。



**方法**

---

`def __init__(self, name="undefined") -> None`

实例化Action。

参数：

+ name：action名称

返回：

+ None

---

`def is_created(self) -> bool`

判断当前 `Action` 是否处于 **CREATED** 状态。

**返回：**

- `bool` — 如果状态为 `ActionStatus.CREATED`，返回 `True`，否则返回 `False`。

------

`def is_undefined(self) -> bool`

判断 `Action` 名称是否为 `"undefined"`。

**返回：**

- `bool` — 如果 `name == "undefined"`，返回 `True`，否则返回 `False`。

------

`def is_running(self) -> bool`

判断当前 `Action` 是否处于 **RUNNING** 状态。

**返回：**

- `bool` — 如果状态为 `ActionStatus.RUNNING`，返回 `True`，否则返回 `False`。

------

`def is_paused(self) -> bool`

判断当前 `Action` 是否处于 **PAUSED** 状态。

**返回：**

- `bool` — 如果状态为 `ActionStatus.PAUSED`，返回 `True`，否则返回 `False`。

------

`def is_stopped(self) -> bool`

判断当前 `Action` 是否已经停止。

**返回：**

- `bool` — 如果 `_stop_event` 已触发，返回 `True`，否则返回 `False`。

------

`def starting_check(self) -> CanStartResult`

检查当前 `Action` 是否允许启动。

**返回：**

- `CanStartResult` —
  - `success()` 表示可以启动
  - `failed(RobotRespCode.XXX)` 表示由于运行中、暂停、已停止或线程存活，无法启动。

------

`def start(self) -> None`

启动当前 `Action`。

**逻辑：**

1. 调用 `starting_check()` 确认能否启动
2. 如果允许，设置状态为 **RUNNING** 并启动新线程
3. 否则直接返回

**返回：**

- `None`

**异常：**

- `RuntimeError` — 如果线程启动失败。

------

`def pause(self) -> None`

暂停当前 `Action`。

**逻辑：**

- 设置状态为 **PAUSED**
- 清除 `_run_event` 阻塞运行

**返回：**

- `None`

------

`def check_pause(self) -> None`

检查是否暂停。

**逻辑：**

- `_run_event._flag`为true不暂停，否则阻塞。

**返回：**

- `None`

------

`def resume(self) -> None`

恢复执行已暂停的 `Action`。

**逻辑：**

- 设置状态为 **RUNNING**
- 重新设置 `_run_event`

**返回：**

- `None`

------

`def before_stop(self) -> None`

在 `stop()` 执行前调用的钩子方法。

**说明：**

- 默认空实现，可在子类中重写，执行资源清理或自定义逻辑。

**返回：**

- `None`

------

`def stop(self) -> None`

停止当前 `Action`。

**逻辑：**

1. 调用 `before_stop()`
2. 设置状态为 **STOPPED**，触发 `_stop_event` 和 `_run_event`
3. 等待线程结束并清理
4. 调用 `after_stop()`
5. 状态恢复为 **CREATED**

**返回：**

- `None`

------

`def after_stop(self) -> None`

在 `stop()` 执行后调用的钩子方法。

**说明：**

- 默认空实现，可在子类中重写，执行收尾逻辑。

**返回：**

- `None`

---

`def proxy_method(self) -> None`

代理执行方法，必须由子类实现。

示例：

```python
def proxy_method(self) -> None:
  while not self.is_stopped():
    for i in range(100):
        self.check_pause()
        print(i)
        time.sleep(1)
  return: None
```



#### `walk_controller.py`

src/w02/walk_controller.py

定义了机器人行走的类，继承Action。

```python
def proxy_method(self) -> None:
    while not self.is_stopped():
        self.check_pause()
        AGC.runActionGroup('go_forward_one_step')
```

重写了proxy_method方法，while循环内一直执行`go_forward_one_step`动作，直到停止或者暂停。



#### `robot_manager.py`

src/w02/robot_manager.py

定义了类RobotManager，作为全局变量，来整合机器人动作控制。



**属性**

`action_dict: dict[ActionGroup, Action]`

动作字典，key是ActionGroup动作组枚举类，val是Action具体的动作控制器。



**方法**

定义了`start_action`、`stop_action`、`pause_action`、`resume_action`四个方法，分别处理机器人动作执行，并且返回结果。



#### 添加路由文件

`src/routes/route_robot.py`

```python
...
robot_bp = Blueprint('robot', __name__)
logger = logging.getLogger(__name__)


@robot_bp.route('/action/start', methods=['POST'])
def start_action() -> Response:
    robot_manager: RobotManager = current_app.robot_manager
    kwargs = request.get_json()
    action_name = kwargs.get('action_name', 'undefined')
    result: Result = robot_manager.start_action(action_name)
    return result
...
```

这里添加了robot_bp作为子路由，用于处理机器人的动作请求。



#### 修改启动命令

`src/app.py`

```python

def init_logger() -> None:
    """
    初始化日志配置
    格式：yy-MM-dd hh:mm:ss name message
    """
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(asctime)s [%(name)s] ===> %(message)s",
        datefmt="%y-%m-%d %H:%M:%S"
    )
     
    
def create_app() -> Flask:
    app = Flask(__name__)
    init_logger()
    app.register_blueprint(robot_bp, url_prefix='/robot')
    app.robot_manager = RobotManager()

    return app

app = create_app()


if __name__ == '__main__':
    app = create_app()
    # 监听所有网络接口，这样局域网内的设备才能访问
    app.run(host='0.0.0.0', port=5000, debug=True)
```

app.py中添加了日志输出的配置，并且将之前写的端点全部移动到路由文件中。在创建app的时候设置robot_manager作为全局变量。



`launch.py`

```python
import subprocess

from src.app import app

if __name__ == '__main__': 
    subprocess.run([
            "gunicorn",
            "--workers", "4",
            "--timeout", "600",
            "--bind", "0.0.0.0:5000",
            "src.app:app"
        ])
```

在launch.py文件中编写启动命令，这样直接运行`python launch.py`就可以启动程序。



## 文件读写

`src/w02/s09_file_rw.py`

在日常编程中，我们经常需要把数据 **保存** 到磁盘，或者从磁盘中 **读取** 已有的数据。
 例如：

- 保存日志、配置文件、用户输入结果
- 读取文本、CSV、JSON 数据用于分析
- 实现简单的数据持久化

在 Python 中，文件操作非常常见，主要通过内置的 `open()` 函数来完成。

**基本语法**：`with open(file,mode,encoding)`：

+ file：文件名称，支持各种格式如：`.txt`、`.json`
+ mode：打开文件模式，常用有：`w`覆盖写、`r`只读、`a`追加写。



### 文件写入

#### 覆盖写入

```python
# 写入文件（覆盖写入模式 "w"）
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("第一行：Hello, Python!\n")
    f.write("第二行：这是文件写入示例。\n")

print("写入完成！")

```



#### 追加写入

```python
# 追加写入模式 "a"
with open("example.txt", "a", encoding="utf-8") as f:
    f.write("第三行：追加内容。\n")

print("追加完成！")
```



### 文件读取

#### 读取整个文件

```python
# 读取文件所有内容
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("文件内容如下：")
print(content)

```



#### 按行读取

```python
# 一行一行读取
with open("example.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("读取到一行：", line.strip())

```



#### 读取为列表

```python
# 读取所有行到列表
with open("example.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("文件行列表：", lines)

```



#### 检查文件是否存在

```python
import os

if os.path.exists("example.txt"):
    print("文件存在！")
else:
    print("文件不存在！")

```







## 代码规范

可参考[python代码规范](./docs/code_standards.md)，来检查项目代码的规范性。



## 练习

+ 利用AI，自行了解容器相关内容：
  + 增删改查
  + 列表：切片、列表推导式、解包等
  + 字典：字典推导式、合并字典、解包等
  + 元组：切片、解包、嵌套元组等

+ 以面向对象的思想，加上机器人的基本控制，设计一个简单的机器人功能模块
+ 提出三个任何与本节内容相关的问题，并自行回答





# OpenCV与机器人视觉（第3周）

## OpenCV简介

**OpenCV (Open Source Computer Vision Library)**。一个开源的 **计算机视觉与图像处理库**。由 Intel 发起，支持 **C++、Python、Java** 等多种语言。可以在 **Windows、Linux、macOS、Android、iOS** 等平台运行

![image-20250929143433195](README_assets/image-20250929143433195.png)



###  OpenCV 的主要功能

1. **图像处理**
   - 图像读写（`cv2.imread`, `cv2.imwrite`）
   - 图像缩放、旋转、裁剪、翻转
   - 颜色空间转换（BGR ↔ Gray, HSV, Lab 等）
   - 滤波与平滑（高斯滤波、均值滤波、中值滤波）
   - 边缘检测（Canny、Sobel 等）
2. **视频处理**
   - 调用摄像头、读取视频文件（`cv2.VideoCapture`）
   - 视频逐帧处理
   - 保存视频（`cv2.VideoWriter`）
3. **特征检测与匹配**
   - 角点检测（Harris、Shi-Tomasi）
   - 特征点提取（SIFT、ORB、FAST）
   - 图像拼接、全景合成
4. **目标检测与识别**
   - 人脸检测（Haar、DNN 模型）
   - 行人检测
   - 深度学习模型推理（支持 TensorFlow / PyTorch 模型）
5. **几何与形状处理**
   - 轮廓检测（`cv2.findContours`）
   - 直线检测（霍夫变换）
   - 图形绘制（直线、圆、矩形、文字等）
6. **机器视觉应用**
   - 运动跟踪
   - 目标分割
   - 增强现实（AR）应用



### 安装

```shell
pip install opencv-python
```



## 图像处理

### 读取图片

```python
import cv2

# 读取图像
img = cv2.imread("tonypi.png")

# 转为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 显示图像
cv2.imshow("Original", img)
cv2.imshow("Gray", gray)

cv2.waitKey(0)  # 等待按键
cv2.destroyAllWindows()

```



### 写入图片

```python
import cv2

img = cv2.imread("tonypi.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_tonypi',img)
```





运行后可以看到两张显示的图片，一张原图，另一张为灰度化后的图：

![image-20250929150101107](README_assets/image-20250929150101107.png)





### 图像缩放

```python
# 缩小为原来一半
small = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# 指定大小 (宽, 高)
resize_200x200 = cv2.resize(img, (200, 200))

cv2.imshow("Resize Small", small)
cv2.imshow("Resize 200x200", resize_200x200)

```



### 图像旋转

#### 固定角度

```python
# 顺时针旋转90度
rotate90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# 逆时针旋转90度
rotate270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Rotate 90", rotate90)
cv2.imshow("Rotate 270", rotate270)

```



#### 任意角度

```python
import numpy as np

(h, w) = img.shape[:2]
center = (w // 2, h // 2)

# 旋转 45 度，缩放 1.0
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotate45 = cv2.warpAffine(img, M, (w, h))

cv2.imshow("Rotate 45", rotate45)

```



### 图像裁剪

```python
# 使用数组切片 [y1:y2, x1:x2]
crop = img[100:300, 200:400]

cv2.imshow("Crop", crop)

```

` img[100:300, 200:400]`可以看成`img[row, coloumn]`，也就是取图片100-300之间的行，和200-400的列。

![image-20250929164343395](README_assets/image-20250929164343395.png)



### 图像翻转

```python
# 水平翻转（左右颠倒）
flip_h = cv2.flip(img, 1)

# 垂直翻转（上下颠倒）
flip_v = cv2.flip(img, 0)

# 水平 + 垂直翻转（180度）
flip_hv = cv2.flip(img, -1)

cv2.imshow("Flip Horizontal", flip_h)
cv2.imshow("Flip Vertical", flip_v)
cv2.imshow("Flip HV", flip_hv)

```

![image-20250929165132301](README_assets/image-20250929165132301.png)



### 图像压缩

运行下面代码，可以看到原图和压缩后的图像，几乎看不出差别，但是压缩后的图像大小相比原图小了很多。

`src/w03/s03_image_compress.py`

```python
import cv2

scale = 0.5  # 缩放到原来的 50%
def show_scaled(win, image, scale):
    h, w = image.shape[:2]
    interp = cv2.INTER_AREA if scale < 1.0 else cv2.INTER_LINEAR
    resized = cv2.resize(image, (int(w*scale), int(h*scale)), interpolation=interp)
    cv2.imshow(win, resized)

img = cv2.imread("../w03/tonypi.png")
# 2. 转换到 YCrCb 颜色空间
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
Y, Cr, Cb = cv2.split(ycrcb)

# 3. 模拟 JPEG 压缩：降低色度分辨率（4:2:0）
Cr_down = cv2.resize(Cr, (Cr.shape[1]//2, Cr.shape[0]//2), interpolation=cv2.INTER_AREA)
Cb_down = cv2.resize(Cb, (Cb.shape[1]//2, Cb.shape[0]//2), interpolation=cv2.INTER_AREA)

# 再上采样回原尺寸
Cr_up = cv2.resize(Cr_down, (Cr.shape[1], Cr.shape[0]), interpolation=cv2.INTER_LINEAR)
Cb_up = cv2.resize(Cb_down, (Cb.shape[1], Cb.shape[0]), interpolation=cv2.INTER_LINEAR)

# 4. 合并回 YCrCb 并转换为 BGR
compressed_ycrcb = cv2.merge([Y, Cr_up, Cb_up])
compressed_img = cv2.cvtColor(compressed_ycrcb, cv2.COLOR_YCrCb2BGR)

show_scaled("ori", img, 0.5)
show_scaled("compressed_img", compressed_img, 0.5)

cv2.imwrite("crowd_compressed.jpeg", compressed_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

```

![image-20251007144820791](README_assets/image-20251007144820791.png)





### 颜色空间转换

>  可以在[颜色代码转换器](https://gradients.app/zh/converter)网站上调试颜色的不同代码。

![image-20250929172611096](README_assets/image-20250929172611096.png)

在OpenCV中，图像默认是BRG格式（不是RGB），可以使用`cv2.cvtColor(img, code)`来进行颜色空间转换。



#### 转换效果示例

```python
import cv2

# 读取一张图像（BGR 格式）
img = cv2.imread("example.jpg")

# 1. BGR → 灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. BGR → HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 3. BGR → Lab
lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

# 4. BGR → RGB（OpenCV 默认 BGR，转 RGB 才能符合常见的 matplotlib 显示习惯）
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 显示结果
cv2.imshow("Original (BGR)", img)
cv2.imshow("Gray", gray)
cv2.imshow("HSV", hsv)
cv2.imshow("Lab", lab)
cv2.imshow("RGB", rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()

```

![image-20250929165602086](README_assets/image-20250929165602086.png)





#### Gray

灰度图，常用于边缘检测、特征提取。



#### HSV

色相-饱和度-亮度，常用于颜色检测（比如提取红色物体）。

+ **H (Hue，色相)**：0–179（在 OpenCV 中范围是 0–179，而不是 0–360）
  - 0 或 180 → 红色
  
  - 30 → 黄色
  
  - 60 → 绿色
  
  - 90 → 青色
  
  - 120 → 蓝色
  
  - 150 → 品红
  
+ **S (Saturation，饱和度)**：0–255（颜色的纯度，越高越鲜艳）

+ **V (Value，明度/亮度)**：0–255（亮度，越高越亮）



##### 示例

HSV=[0, 120, 70] 它通常作为 **红色的下界阈值**，在 OpenCV 里，为了提取红色，可以这样写：

```python
lower_red = np.array([0, 120, 70])    # 红色的低范围
upper_red = np.array([10, 255, 255])  # 红色的高范围
mask1 = cv2.inRange(hsv, lower_red, upper_red)

```



#### Lab

感知均匀的颜色空间，常用于图像增强和风格转换。



#### RGB ↔ BGR

主要用于兼容 matplotlib 和其他库。





#### 练习

##### 灰度化（BGR → Gray）

灰度图像减少了颜色信息，只保留亮度，方便计算。应用在人脸识别、边缘检测、OCR 等。

```python
import cv2

img = cv2.imread("../w03/crowd.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

![image-20250930144608982](README_assets/image-20250930144608982.png)



##### 图像增强（HSV/Lab）

应用：改善亮度、对比度，提升夜间图像效果。

- 在 HSV 中，调整 **V 通道** 可以整体提升亮度。
- 在 Lab 空间中，**L 通道**表示亮度，更容易做光照校正。

```python
import cv2

scale = 0.5  # 缩放到原来的 50%
def show_scaled(win, image, scale):
    h, w = image.shape[:2]
    interp = cv2.INTER_AREA if scale < 1.0 else cv2.INTER_LINEAR
    resized = cv2.resize(image, (int(w*scale), int(h*scale)), interpolation=interp)
    cv2.imshow(win, resized)

img = cv2.imread("../w03/night.jpeg")
# BGR -> HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 提升亮度
h, s, v = cv2.split(hsv)
v = cv2.equalizeHist(v)  # 直方图均衡化
enhanced_hsv = cv2.merge([h, s, v])

# 转回 BGR
enhanced = cv2.cvtColor(enhanced_hsv, cv2.COLOR_HSV2BGR)

show_scaled("ori", img, 0.5)
show_scaled("enhanced", enhanced, 0.5)

cv2.waitKey(0)
cv2.destroyAllWindows()

```



![image-20250930145729426](README_assets/image-20250930145729426.png)



##### 颜色校准

应用：相机拍照时颜色偏差修复、不同相机风格统一。例如：在 Lab 空间里调整 **a、b 通道**，可以让图像更“暖”或更“冷”。

```python
import cv2

scale = 0.5  # 缩放到原来的 50%
def show_scaled(win, image, scale):
    h, w = image.shape[:2]
    interp = cv2.INTER_AREA if scale < 1.0 else cv2.INTER_LINEAR
    resized = cv2.resize(image, (int(w*scale), int(h*scale)), interpolation=interp)
    cv2.imshow(win, resized)

img = cv2.imread("../w03/crowd.jpeg")
lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

l, a, b = cv2.split(lab)


# 调整 a、b 实现偏色修复（如减少绿色、增加红色）
a = cv2.add(a, 10)
b = cv2.subtract(b, 10)

corrected_lab = cv2.merge([l, a, b])
corrected = cv2.cvtColor(corrected_lab, cv2.COLOR_Lab2BGR)


show_scaled("ori", img, 0.5)
show_scaled("lab", corrected, 0.5)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

将 Lab 图像分离为三个独立通道：

- **L 通道**：亮度（Lightness，0-100）
- **a 通道**：绿色 ↔ 红色（-128 到 +127）
- **b 通道**：蓝色 ↔ 黄色（-128 到 +127

![image-20250930151138282](README_assets/image-20250930151138282.png)







##### 提取图像中红色部分

```python
import cv2
import numpy as np
# 读取图像
img = cv2.imread("tonypi.png")

# BGR → HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 红色范围（低阈值 & 高阈值）
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

lower_red = np.array([170, 120, 70])
upper_red = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, lower_red, upper_red)

# 合并两个红色区间
mask = mask1 + mask2

# 提取红色区域
red_region = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Red Region", red_region)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

![image-20250930143813618](README_assets/image-20250930143813618.png)







灰度化：减少计算量

模糊：去除噪声

边缘检测：用于检测地面边界、障碍物



## 视频处理

### 打开机器人摄像头

使用opencv打开摄像头十分方便，使用VNC连接机器人桌面，运行以下代码，即可打开机器人摄像头并显示拍摄画面：

`scr/w03/s02_open_camera.py`

```python
import cv2

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Client", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
```

![image-20250929152057748](README_assets/image-20250929152057748.png)



### 分发摄像头画面

对于比较复杂的、计算资源消耗较高的图像处理操作，机器人自身硬件处理可能比较慢，我们可以使用电脑来进行处理。这时需要将机器人摄像头拍摄的画面分发给电脑。我们使用socket服务端与客户端来实现视频流分发与接收。

整理逻辑：摄像头获取图像后，服务端对图像编码转为字节流通过TCP连接分发。客户端与服务端建立连接获取字节流，解码为视频流，进行后处理。

![video_distribute](README_assets/video_distribute-17598188680759.jpg)

#### 服务端

在机器人上运行服务端：

`src/w03/s02_video_server.py`

```python
import cv2
import socket
import struct

# 创建 socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("0.0.0.0", 8888))  # 监听所有网卡的 8888 端口
server_socket.listen(1)

print("等待客户端连接...")
conn, addr = server_socket.accept()
print("客户端已连接：", addr)

cap = cv2.VideoCapture(0)  # 读取摄像头（0）或视频文件

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 压缩为 JPG，80表示图片质量，0-100，越大越清晰，文件也更大
    ret, buffer = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
    data = buffer.tobytes()

    # 先发送长度，再发送数据
    conn.sendall(struct.pack(">I", len(data)) + data)

cap.release()
conn.close()
server_socket.close()

```



#### 客户端

在电脑上运行客户端，注意将`client_socket.connect(("127.0.0.1", 8888))`中的ip改为机器人的ip地址。

`src/w03/s02_video_client.py`

```python
import cv2
import socket
import struct
import numpy as np

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8888))  # 例如 ("127.0.0.1", 8888)

while True:
    # 先接收 4 字节长度
    data_len = client_socket.recv(4)
    if not data_len:
        break

    length = struct.unpack(">I", data_len)[0]

    # 再接收对应长度的数据
    data = b""
    while len(data) < length:
        packet = client_socket.recv(length - len(data))
        if not packet:
            break
        data += packet

    # 解码为图像
    img_array = np.frombuffer(data, dtype=np.uint8)
    frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    # 显示图像
    cv2.imshow("Client", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

client_socket.close()
cv2.destroyAllWindows()

```



服务端、客户端启动后就可以在电脑上看见机器人摄像头所拍摄的画面。



## 绘制图形

OpenCV 不仅能读取和处理图像，也可以直接在图像上绘制各种几何图形。

| 功能     | 函数              |
| -------- | ----------------- |
| 画线     | `cv2.line()`      |
| 画矩形   | `cv2.rectangle()` |
| 画圆     | `cv2.circle()`    |
| 画椭圆   | `cv2.ellipse()`   |
| 画多边形 | `cv2.polylines()` |
| 文字     | `cv2.putText()`   |



| 参数        | 含义           | 示例                                  |
| ----------- | -------------- | ------------------------------------- |
| `color`     | 颜色，BGR 格式 | `(255,0,0)` 蓝色                      |
| `thickness` | 线宽（像素）   | `1`、`2`、`-1`（填充）                |
| `lineType`  | 线条样式       | `cv2.LINE_8`、`cv2.LINE_AA`（抗锯齿） |



运行下面代码，可以看到简单的绘制效果。

`src/w03/s04_draw.py`

```python
import cv2
import numpy as np

# 1. 创建黑色背景图像 (512x512, 3通道, uint8)
img = np.zeros((512, 512, 3), dtype=np.uint8)

# 2. 绘制直线
cv2.line(img, (50, 100), (450, 100), (0, 255, 0), thickness=3)
# 参数说明：
# (50,100) 起点坐标
# (450,100) 终点坐标
# (0,255,0) 颜色：BGR = 绿色
# thickness=3 线宽为3像素

# 3. 绘制矩形
cv2.rectangle(img, (100, 150), (400, 300), (255, 0, 0), thickness=2)
# 若 thickness = -1 则填充矩形

# 4. 绘制圆形
cv2.circle(img, (256, 400), 50, (0, 0, 255), thickness=-1)
# thickness=-1 表示实心圆

# 5. 绘制椭圆
cv2.ellipse(img, (256, 256), (100, 50), 45, 0, 360, (255, 255, 0), 2)
# 中心点 (256,256)，长短轴(100,50)，旋转45°

# 6. 绘制多边形
pts = np.array([[100,400], [200,350], [300,400], [250,450], [150,450]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], isClosed=True, color=(255, 255, 255), thickness=2)

# 7. 添加文字
cv2.putText(img, "OpenCV Drawing Demo", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
            1, (0, 255, 255), 2, cv2.LINE_AA)
# 参数说明：
# (50,50) 文本左下角坐标
# 字体类型、字体大小、颜色、线宽、抗锯齿

# 8. 显示结果
cv2.imshow("Drawing Demo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

![image-20251007150229753](README_assets/image-20251007150229753.png)





## 形状与轮廓检测

在计算机视觉中，**轮廓（Contour）** 是指图像中连续边缘的曲线，它能有效地描述一个物体的**形状和结构特征**。

OpenCV 提供了非常强大的轮廓检测函数 `cv2.findContours()`，常用于以下任务：

- **形状识别**（判断圆形、矩形、三角形等）
- **目标分割**（检测物体区域）
- **测量与检测**（计算面积、周长、位置）
- **图像特征提取**（如边缘点、边界框）



### 具体流程

#### 图像二值化

轮廓检测的前提是：**黑白分明的二值图像**（即只有 0 和 255 两种像素值）。因为 OpenCV 会在“颜色变化的边界”上寻找连续的像素点作为轮廓。

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
```

这一步中：

- `cv2.threshold()` 把灰度图转为二值图；
- 白色（255）表示目标；
- 黑色（0）表示背景。

二值化后概是这样：

| 灰度图          | 二值图      |
| --------------- | ----------- |
| 122 134 180 220 | 0 0 255 255 |

只有白色区域才被认为是“要检测的对象”。

![image-20251007203401201](README_assets/image-20251007203401201.png)



####  边界追踪（Contour Tracing）

`cv2.findContours()` 的核心任务是：

> 从二值图中，沿着目标的边界像素连续地走一圈，把轮廓点记录下来。

算法原理来自于 **Suzuki & Abe 算法（1985）**，
 它的思想是：

> 从左上角开始扫描，遇到白点 → 判断它是否是新轮廓的起点 →若是，就开始沿边缘方向（顺时针）跟踪，直到回到起点为止。

最终，它返回所有目标的边界点序列。

如：

```python
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
```

此时 `contours` 是一个“轮廓列表”，每个元素都是一个 numpy 数组，包含该轮廓的所有像素坐标点，这些点就是目标形状的边界：

```python
array([[[51, 220]], [[52, 219]], [[53, 218]], ...], dtype=int32)
```



#### 判断轮廓的形状

OpenCV 不会直接告诉你“这是个矩形”或“这是个三角形”，它只是告诉你这个轮廓的点在哪里。 **形状判断**是通过对这些点做几何分析得到的。

##### 多边形拟合：`cv2.approxPolyDP`

轮廓往往包含很多噪声点，例如矩形的边缘可能有几十个点。为了方便识别，需要“简化”轮廓。

```python
epsilon = 0.02 * cv2.arcLength(contour, True)
approx = cv2.approxPolyDP(contour, epsilon, True)
```

+ `cv2.arcLength(contour, True)` 计算轮廓的**周长**；

+ `epsilon` 是近似精度（比例越大，形状越粗糙）；

+ `cv2.approxPolyDP()` 通过 **Ramer–Douglas–Peucker 算法** 对曲线进行“折线近似”；它会用更少的点（顶点）来表示同样的形状。

最终结果：

| 原轮廓点 | 近似后顶点数 | 推测形状     |
| -------- | ------------ | ------------ |
| 150 点   | 3            | 三角形       |
| 200 点   | 4            | 矩形或正方形 |
| 500 点   | >5           | 圆形或椭圆   |



##### 顶点数判断

我们根据 `len(approx)`（顶点数量）来判断形状：

```python
sides = len(approx)
if sides == 3:
    shape = "Triangle"
elif sides == 4:
    shape = "Rectangle / Square"
elif sides > 5:
    shape = "Circle"
```



##### 判断正方形 vs 矩形

对于 4 个顶点的情况，需要进一步判断长宽比例：

```python
x, y, w, h = cv2.boundingRect(approx)
aspect_ratio = w / float(h)
if 0.95 < aspect_ratio < 1.05:
    shape = "Square"
else:
    shape = "Rectangle"
```

+ `cv2.boundingRect()` 会给出最小外接矩形；

+ **长宽比接近 1 → 正方形**。



##### 判断圆形：面积比法

当轮廓点很多时（近似为圆），我们可以通过**面积对比**来判断：

```python
area = cv2.contourArea(contour)
(x, y), radius = cv2.minEnclosingCircle(contour)
circle_area = np.pi * (radius ** 2)

circularity = area / circle_area
if circularity > 0.8:
    shape = "Circle"
```

如果轮廓的面积与外接圆面积非常接近，说明它很“圆滑”，即为圆形。



#### 获取形状位置（中心点）

`cv2.moments()` 可以用来计算**轮廓的几何矩（moments）**，这些矩可以用来求取形心（质心）坐标。

> **零阶矩（m00m00）**‌：表示轮廓面积。
>
> ‌**一阶矩（m10m10 和 m01m01）**‌：用于计算质心坐标，公式为$X_{c}=\frac{M_{10}}{M_{00}} $，$Y_{c}=\frac{M_{01}}{M_{00}} $。
>
> ‌**二阶矩（m20m20、m02m02、m11m11）**‌：关联旋转半径、长轴、短轴等特征。 
>
> ‌**三阶矩（m30m30、m03m03、m21m21、m12m12）**‌：反映轮廓的扭曲程度或斜度。

```python
M = cv2.moments(contour)
cx = int(M["m10"] / M["m00"])
cy = int(M["m01"] / M["m00"])
```

这样我们就得到了每个形状的中心点，可以在图像上标注文字：

```python
cv2.putText(img, shape, (cx - 30, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
```



### 示例

运行下面代码，可以看到检测后的轮廓效果：

`src/w03/s05_contour.py`

```python
import cv2
import numpy as np

# 1️⃣ 读取图像
img = cv2.imread("contour.png")  # 图像中包含圆形、矩形、三角形等
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# 2️⃣ 转为二值图像（阈值分割）
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold", thresh)

# 3️⃣ 提取轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 4️⃣ 遍历每个轮廓并判断形状
for contour in contours:
    # 计算近似多边形
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # 绘制轮廓
    cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)

    # 计算轮廓中心
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    else:
        cx, cy = 0, 0

    # 根据顶点数判断形状
    sides = len(approx)
    shape = "Unknown"
    if sides == 3:
        shape = "Triangle"
    elif sides == 4:
        # 判断矩形还是正方形
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        shape = "Square" if 0.95 < aspect_ratio < 1.05 else "Rectangle"
    elif sides > 5:
        shape = "Circle"

    # 绘制文字
    cv2.putText(img, shape, (cx - 40, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

# 5️⃣ 显示结果
cv2.imshow("Detected Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

![image-20251007205334636](README_assets/image-20251007205334636.png)





## 颜色识别

颜色识别是 OpenCV 图像处理中的一个核心应用，之前在`颜色空间转换`已经提及，它的本质就是：

>  在 **颜色空间（通常是 HSV）** 中筛选出特定颜色范围的像素区域。



### 基本原理

我们用 **HSV 颜色空间**（Hue、Saturation、Value） 来识别颜色。

相比 BGR：

- H（色相）代表颜色类型（红、绿、蓝等）
- S（饱和度）代表颜色的纯度
- V（亮度）代表颜色的明暗

> 在 HSV 空间中，红色、蓝色、绿色等颜色有相对稳定的“范围区间”，所以比直接用 RGB/BGR 更容易筛选。



### 示例

参考之前练习：[提取颜色示例](#提取图像中红色部分)。



### 常用颜色HSV区间

| 颜色 | H 范围             | S/V                 |
| ---- | ------------------ | ------------------- |
| 红色 | [0,10] ∪ [170,180] | S:120-255, V:70-255 |
|绿色|	[36, 86]	|S: 25-255, V: 25-255|
|蓝色|	[94, 126]	|S: 80-255, V: 2-255|
|黄色|	[15, 35]	|S: 100-255, V: 100-255|
|橙色|	[10, 25]	|S: 150-255, V: 100-255|
|紫色|	[125, 155]	|S: 100-255, V: 100-255|



## 人脸检测

“人脸检测（Face Detection）” 是 OpenCV 最常用、最经典的计算机视觉功能之一。它可以用于：

- 摄像头实时人脸识别
- 拍照自动对焦
- 表情分析、身份验证等场景。



### 基本原理

OpenCV 提供了两种常见的人脸检测方法：

| 方法                                | 模型                    | 特点                     |
| ----------------------------------- | ----------------------- | ------------------------ |
| **Haar 级联分类器（Haar Cascade）** | 传统机器学习            | 快速、轻量、易用         |
| **DNN（深度学习检测）**             | Caffe / TensorFlow 模型 | 精度高、抗光照强、但较慢 |

我们先介绍 **Haar 级联检测**，这是最经典的入门方法。



### 模型文件

OpenCV 内置了人脸检测模型文件： `haarcascade_frontalface_default.xml`

你可以在安装目录下找到它，

执行：

```python
ls /home/pi/.local/lib/python3.11/site-packages/cv2/data
```

可以看到这个模型文件：

```shell
haarcascade_eye_tree_eyeglasses.xml      haarcascade_license_plate_rus_16stages.xml
haarcascade_eye.xml                      haarcascade_lowerbody.xml
haarcascade_frontalcatface_extended.xml  haarcascade_profileface.xml
haarcascade_frontalcatface.xml           haarcascade_righteye_2splits.xml
haarcascade_frontalface_alt2.xml         haarcascade_russian_plate_number.xml
haarcascade_frontalface_alt_tree.xml     haarcascade_smile.xml
haarcascade_frontalface_alt.xml          haarcascade_upperbody.xml
haarcascade_frontalface_default.xml      __init__.py
haarcascade_fullbody.xml                 __pycache__
haarcascade_lefteye_2splits.xml
╭─  │  ~/miniconda3/envs/myvenv01                                  ✔ │ myvenv01  │ pi@raspberrypi │ 00:16:35  
╰─ 
```

在代码中使用相对路径：

```python
cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
```



### 示例

运行下面代码，可以看到图片中的人脸被绿色矩形框标出。



```python
import cv2

# 加载人脸分类器
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# 读取图像并转灰度
img = cv2.imread("huge.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 检测人脸
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,   # 每次图像尺寸缩小的比例
    minNeighbors=5,    # 保留候选框的最小邻居数（越大越严格）
    minSize=(30, 30)   # 最小检测人脸尺寸
)

# 绘制检测框
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 显示结果
cv2.imshow("Detected Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

![image-20251007211749047](README_assets/image-20251007211749047.png)



### 参数调整

| 参数           | 说明             | 调整方向            |
| -------------- | ---------------- | ------------------- |
| `scaleFactor`  | 图像每次缩小比例 | 小 → 精度高但慢     |
| `minNeighbors` | 检测框合并阈值   | 大 → 更严格，误检少 |
| `minSize`      | 最小人脸尺寸     | 小 → 可检测远处人脸 |



## 目标跟踪

“目标跟踪（Object Tracking）” 是计算机视觉中与检测密切相关的核心任务之一。它的作用是：**在视频中持续追踪一个或多个移动目标**（如人、车、球等）。

### 安装tracking模块

安装带有 tracking 模块的opencv版本：

```python
pip install --upgrade --force-reinstall opencv-contrib-python==4.10.0.84
```



### 目标跟踪简介

目标跟踪是指在视频帧序列中，识别并持续跟踪某个已检测到的物体。OpenCV 提供了多种跟踪算法，通过 `cv2.legacy.Tracker_xxx_create()` 来调用。

### 常见的跟踪算法

| 算法名称       | 特点                         |
| -------------- | ---------------------------- |
| **BOOSTING**   | 较早版本，速度慢但简单       |
| **MIL**        | 可在部分遮挡情况下继续跟踪   |
| **KCF**        | 性能好，速度快（常用）       |
| **TLD**        | 可重新检测丢失目标           |
| **MedianFlow** | 稳定性好，但对快速运动敏感   |
| **MOSSE**      | 极快（实时性高），轻量级     |
| **CSRT**       | 精度最高，但速度略慢（推荐） |



### 核心流程

1. 读取视频流或摄像头输入
2. 选择目标区域（ROI）
3. 初始化跟踪器
4. 逐帧更新并绘制跟踪框



### 示例（使用CSRT算法

示例使用了一段街道的视频作为视频流输入。运行下面代码，首先需要选取一个区域，作为跟踪的目标，按住鼠标左键，拖拽到合适位置，松开，选择需要追踪区域。

![image-20251007214053360](README_assets/image-20251007214053360.png)



然后按下空格/回车，开始追踪目标。

![image-20251007214211428](README_assets/image-20251007214211428.png)



```python
import cv2

# 打开视频（或使用摄像头）
cap = cv2.VideoCapture("stree.mp4")  # 可改成 "video.mp4"

# 读取第一帧
ret, frame = cap.read()
if not ret:
    print("无法读取视频源")
    exit()

# 手动选择跟踪目标（ROI：Region of Interest）
bbox = cv2.selectROI("请选择跟踪目标", frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("请选择跟踪目标")

# 创建跟踪器（推荐 CSRT）
tracker = cv2.legacy.TrackerCSRT_create()
ok = tracker.init(frame, bbox)

# 逐帧更新跟踪
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 更新跟踪结果
    ok, bbox = tracker.update(frame)

    if ok:
        # 如果成功跟踪，绘制矩形框
        x, y, w, h = map(int, bbox)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Tracking", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    else:
        # 跟踪失败
        cv2.putText(frame, "Lost", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Object Tracking", frame)

    # 按 ESC 退出
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

```



## 练习

+ 使用本节内容设计一个与机器人视觉相关的功能模块
+ 提出三个任何与本节内容相关的问题，并自行回答



# 机器人语音识别与语音合成（第4周）

## 固件烧录

首先将 WonderEcho Pro 通过 Type-C 数据线连接至电脑。

![image-20251008152000027](README_assets/image-20251008152000027.png)

打 开 “ 10.1.5 附 录 \ 固 件 烧 录 工 具 ” 下 的 “ **固 件 烧 录 工 具\PACK_UPDATE_TOOL.exe**”文件，选择“**CI1302**”芯片，然后点击“**固件升级**”。

![image-20251008152054744](README_assets/image-20251008152054744.png)



### 查看串口

找到"**10.1.5 附录\串口调试助手\serial_port_utility_603_0103.exe**"安装程序，点击安装，打开。

在“端口”中选择“**USB-SERIAL CH340**”，前面显示的串口就是烧录时要选择的串口。

![image-20251008152513051](README_assets/image-20251008152513051.png)

![image-20251008152456591](README_assets/image-20251008152456591.png)

### 烧录

在**10.1.5 附录**文件夹下选择中文“小幻小幻”唤醒的固件。

![image-20251008152847780](README_assets/image-20251008152847780.png)



选择**USB-SERIAL CH340对应的串口**，勾选。

![image-20251008152958262](README_assets/image-20251008152958262.png)



接着按下语音交互模块上的 **RST** **键**，即可进入到烧录中，等待烧录成功即可。

![image-20251008153112693](README_assets/image-20251008153112693.png)

![image-20251008153122622](README_assets/image-20251008153122622.png)





## 语音模块安装

使用 M4*6 的圆头螺丝将 AI 语音交互盒（WonderEcho Pro）安装在 TonyPi 的背部，注意安装方向。

![image-20251008153222819](README_assets/image-20251008153222819.png)



通过 Type C 线，将模块连接到机器人的 USB 口。

![image-20251008153239491](README_assets/image-20251008153239491.png)



### 测试

vnc 远程连接桌面进入树莓派系统，查看右上角是否有麦克风好扬声器的标志。如下图所示，有即代表连接成功。

![image-20251008153351202](README_assets/image-20251008153351202.png)



### 录音

在终端输入：

```shell
arecord -l
```

输出：

```shell
**** List of CAPTURE Hardware Devices ****
card 2: Device [USB PnP Audio Device], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

`card 2` 可以看到卡号为2。

执行命令录音。ctrl+C停止：

```
arecord -D hw:2,0 -f S16_LE -r 16000 -c 2 test.wav
```

录音完成之后，当前文件夹下会有一个test.wav，播放这个音频文件，可以听到刚才录制的声音。





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





# 附录

## 预设动作



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
| move_up                    | 蹲下，抱球，站起，将手举到头顶 |  |
| put_down_object            | 蹲下，身体前倾，伸出右手 | put_up_object恢复站立 |
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





