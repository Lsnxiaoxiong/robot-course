import socket
import threading
import numpy as np
import sounddevice as sd
from src.w08.touch_sensor import TouchSensor


def send_audio_client(server_ip, port=50007):
    """音频发送客户端：连接到服务器，录音并发送"""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, port))
    print(f"已连接到服务器: {server_ip}")

    stream = sd.InputStream(samplerate=16000, channels=1, dtype="int16",
                            blocksize=9600)
    stream.start()
    try:
        while True:
            audio_data, _ = stream.read(9600)
            client.sendall(audio_data.astype("int16").tobytes())
    except Exception as e:
        print("发送客户端断开:", e)
    finally:
        stream.stop()
        client.close()


def receive_audio_client(server_ip, port=50008):
    """音频接收客户端：连接到服务器，接收并播放"""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, port))
    print(f"已连接到服务器: {server_ip}")

    stream = sd.OutputStream(samplerate=24000, channels=1, dtype="float32",
                             blocksize=2048)
    stream.start()
    try:
        while True:
            data = client.recv(8192)
            if not data:
                break
            stream.write(np.frombuffer(data, dtype="float32"))
    except Exception as e:
        print("接收客户端断开:", e)
    finally:
        stream.stop()
        client.close()


if __name__ == "__main__":
    threading.Thread(target=receive_audio_client, args=("10.127.194.224",)).start()
    threading.Thread(target=send_audio_client, args=("10.127.194.224",)).start()
    TouchSensor(pin=22, buzzer_enabled=True).start()