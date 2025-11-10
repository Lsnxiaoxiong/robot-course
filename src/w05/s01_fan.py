from gpiozero import OutputDevice
from time import sleep

# gpiozero 默认使用 BCM 编号，我们直接指定引脚号
# gpiozero uses BCM numbering by default, we just specify the pin numbers
fanPin1 = OutputDevice(8)
fanPin2 = OutputDevice(7)


# fan control
def set_fan(start):
    if start == 1:
        ## 开启风扇, 顺时针(turn on the fan, clockwise)
        print("Turning fan ON")
        fanPin1.on()  # 等同于输出高电平 (Equivalent to outputting HIGH)
        fanPin2.off()  # 等同于输出低电平 (Equivalent to outputting LOW)
    else:
        ## 关闭风扇(turn off the fan)
        print("Turning fan OFF")
        fanPin1.off()  # 等同于输出低电平 (Equivalent to outputting LOW)
        fanPin2.off()  # 等同于输出低电平 (Equivalent to outputting LOW)


if __name__ == '__main__':
    try:
        # 初始状态，关闭风扇
        set_fan(0)
        sleep(1)

        # 开启风扇并保持运行
        set_fan(1)
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Turning fan off.")
        # gpiozero 会在程序结束时自动清理资源，但手动关闭更保险
        # gpiozero cleans up resources automatically on exit, but manual shutdown is safer
        set_fan(0)