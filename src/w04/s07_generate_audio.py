import socket
import threading
import time

import numpy as np

from src.w04.robot_audio import RobotAudio
from src.w04.s06_kokoro import AudioGenerator

import sounddevice as sd

audio_generator = None

def generate():
    # 注意：这里的 50007 应该是整数端口号
    HOST = '192.168.137.95'
    PORT = 50007

    client = None  # 初始化 client 变量
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        print(f"成功连接到服务器 {HOST}:{PORT}")

        audio_generator = AudioGenerator()
        audio_generator.start_generate()
        # 假设在开始生成前，你需要推入文本
        audio_generator.push_text("你好，这是一个测试音频。")

        print("开始发送音频数据...")

        for audio_chunk in audio_generator.get_audio():
            if audio_chunk is not None:
                # 将 numpy 数组转换为 bytes 对象进行网络传输
                # 如果 audio_chunk 已经是 bytes，则不需要 tobytes()
                # 根据 AudioGenerator 的上下文，它大概率是 numpy 数组
                audio_bytes = audio_chunk.numpy().tobytes()
                # 发送数据块
                client.sendall(audio_bytes)
                # 理论上可以添加一个小的延时，但对于音频流一般不加
            else:
                # 收到 None 退出信号
                print("收到音频生成结束信号。")
                break

        print("音频数据发送完成。")

    except ConnectionRefusedError:
        print("连接被拒绝，请检查服务器是否正在运行以及IP地址和端口是否正确。")
    except Exception as e:
        print(f"发送过程中发生错误: {e}")
    finally:
        # 确保关闭连接
        if client:
            client.close()
            print("Socket 连接已关闭。")

def play():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 50007))
    server.listen(1)
    print(f"接收服务端启动，等待连接...")
    conn, addr = server.accept()
    print(f"客户端已连接: {addr}")

    stream = sd.OutputStream(samplerate=24000, channels=1, dtype="float32",
                             blocksize=2048)
    stream.start()
    try:
        while True:
            data = conn.recv(8192)
            if not data:
                break
            stream.write(np.frombuffer(data, dtype="float32"))
    except Exception as e:
        print("接收服务端断开:", e)
    finally:
        stream.stop()
        conn.close()
        server.close()


if __name__ == '__main__':
    # threading.Thread(target=play).start()
    time.sleep(1)

    generate()

    # text = ""
    # while True:
    #     text = input("请输入要转换的文本：")
    #     audio_generator.push_text()