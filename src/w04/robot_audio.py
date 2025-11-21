import socket
import numpy as np
import sounddevice as sd


class RobotAudio:

    def __init__(self):
        self.host = "0.0.0.0"
        self.port = 50007
        self.SAMPLE_RATE = 16000
        self.FRAME_LEN = 960  # 60ms = 960 采样点
        self.chunk_size = [0, 10, 5]
        self.CHUNK_FRAMES = self.chunk_size[1]  # 10 帧
        self.chunk_stride = self.CHUNK_FRAMES * self.FRAME_LEN  # = 9600 采样点 ≈ 600ms

    def send_audio_server(self):
        """音频发送服务端：监听连接，录音并发送"""
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(1)
        print(f"发送服务端启动，等待连接...")
        conn, addr = server.accept()
        print(f"客户端已连接: {addr}")

        stream = sd.InputStream(samplerate=self.SAMPLE_RATE, channels=1, dtype="int16",
                                blocksize=self.chunk_stride)
        stream.start()
        try:
            while True:
                audio_data, _ = stream.read(self.chunk_stride)
                conn.sendall(audio_data.astype("int16").tobytes())
        except Exception as e:
            print("发送服务端断开:", e)
        finally:
            stream.stop()
            conn.close()
            server.close()

    def send_audio_client(self, server_ip):
        """音频发送客户端：连接到服务器，录音并发送"""
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server_ip, self.port))
        print(f"已连接到服务器: {server_ip}")

        stream = sd.InputStream(samplerate=self.SAMPLE_RATE, channels=1, dtype="int16",
                                blocksize=self.chunk_stride)
        stream.start()
        try:
            while True:
                audio_data, _ = stream.read(self.chunk_stride)
                client.sendall(audio_data.astype("int16").tobytes())
        except Exception as e:
            print("发送客户端断开:", e)
        finally:
            stream.stop()
            client.close()

    def receive_audio_server(self):
        """音频接收服务端：监听连接，接收并播放"""
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', self.port))
        server.listen(1)
        print(f"接收服务端启动，等待连接...")
        conn, addr = server.accept()
        print(f"客户端已连接: {addr}")

        stream = sd.OutputStream(samplerate=self.SAMPLE_RATE, channels=1, dtype="int16",
                                 blocksize=self.chunk_stride)
        stream.start()
        try:
            while True:
                data = conn.recv(self.chunk_stride * 2)  # int16 = 2 bytes
                if not data:
                    break
                stream.write(np.frombuffer(data, dtype="int16"))
        except Exception as e:
            print("接收服务端断开:", e)
        finally:
            stream.stop()
            conn.close()
            server.close()

    def receive_audio_client(self, server_ip):
        """音频接收客户端：连接到服务器，接收并播放"""
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server_ip, self.port))
        print(f"已连接到服务器: {server_ip}")

        stream = sd.OutputStream(samplerate=self.SAMPLE_RATE, channels=1, dtype="int16",
                                 blocksize=self.chunk_stride)
        stream.start()
        try:
            while True:
                # data = client.recv(self.chunk_stride * 2)  # int16 = 2 bytes
                data = client.recv(960)  # int16 = 2 bytes
                if not data:
                    break
                stream.write(np.frombuffer(data, dtype="int16"))
        except Exception as e:
            print("接收客户端断开:", e)
        finally:
            stream.stop()
            client.close()


# 使用示例
if __name__ == "__main__":
    robot = RobotAudio()

    # 根据需要选择运行模式：
    # robot.send_audio_server()              # 作为发送服务端
    # robot.send_audio_client("192.168.1.100")  # 作为发送客户端
    # robot.receive_audio_server()           # 作为接收服务端
    robot.receive_audio_client("192.168.1.104")  # 作为接收客户端