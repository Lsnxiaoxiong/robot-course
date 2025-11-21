import queue
import socket
import threading
import time
from typing import Optional


class SocketServer:

    def __init__(self, host: str = "0.0.0.0", port: int = 8888):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print(f"服务器启动，监听 {self.host}:{self.port}")
        self.conn, self.addr = self.socket.accept()
        print(f"已连接: {self.addr}")
        self.received_msg: queue.Queue = queue.Queue()
        self._recv_thread: Optional[threading.Thread] = threading.Thread(target=self.receive_msg).start()

    def recv_exact(self, n_bytes):
        buffer = b""
        while len(buffer) < n_bytes:
            packet = self.conn.recv(n_bytes - len(buffer))  # 每次只申请剩下的字节数
            if not packet:  # 读取到空字节表示对端关闭
                raise ConnectionError("Socket connection broken")
            buffer += packet
        return buffer

    def receive_msg(self):
        try:
            while True:
                try:
                    # 先接收4字节长度
                    length_bytes = self.conn.recv(4)
                    if not length_bytes:
                        print("客户端断开连接")
                        raise ConnectionError("Socket connection broken")
                    length = int.from_bytes(length_bytes, 'big')  # 或者 'little'，双方要一致
                    # 再接收实际字符串内容
                    data = self.recv_exact(length)

                    message = data.decode('utf-8')
                    if message != "":
                        self.received_msg.put(message)
                        print(f"收到消息: {message}")
                except:
                    print("服务器断开连接")
                    self.conn.close()
                    self.conn, self.addr = self.socket.accept()
                    print(f"已连接: {self.addr}")
        finally:
            self.conn.close()
            self.socket.close()


if __name__ == "__main__":
    server = SocketServer()
    # server.receive_msg()
    # time.sleep(100)
# 创建服务器 socket
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('0.0.0.0', 8888))  # 监听本地 8888 端口
# server.listen(5)
# print("服务器启动，等待连接...")
#
# conn, addr = server.accept()  # 接受客户端连接
# print(f"连接来自: {addr}")
#
# while True:
#     # 先接收4字节长度
#     length_bytes = conn.recv(4)
#     if not length_bytes:
#         print("客户端断开连接")
#         break
#     length = int.from_bytes(length_bytes, 'big')  # 或者 'little'，双方要一致
#     # 再接收实际字符串内容
#     data = b''
#     while len(data) < length:
#         packet = conn.recv(length - len(data))
#         if not packet:
#             break
#         data += packet
#
#     if len(data) < length:
#         print("接收不完整")
#         break
#
#     message = data.decode('utf-8')
#     print(f"收到消息: {message}")
#
#     # 回显给客户端（可选）
#     response = "我收到啦: " + message
#     response_bytes = response.encode('utf-8')
#     conn.send(len(response_bytes).to_bytes(4, 'big'))  # 先发长度
#     conn.send(response_bytes)  # 再发内容
#
# conn.close()
# server.close()