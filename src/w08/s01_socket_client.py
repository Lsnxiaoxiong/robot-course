import queue
import socket
import threading
import time


class SocketClient:
    MAX_RECONNECT_TRIES = 5

    def __init__(self, host: str = "127.0.0.1", port: int = 8888):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.msg_queue = queue.Queue()
        self._send_pause = threading.Event()
        self._send_pause.set()

        self.connet()
        self._send_thread = None

    def connet(self):
        cur_reconnect_tries = 0
        while cur_reconnect_tries < self.MAX_RECONNECT_TRIES:
            try:
                self.socket.connect((self.host, self.port))
                self._send_thread = threading.Thread(target=self.send_msg).start()
                break
            except Exception as e:
                cur_reconnect_tries += 1
                print(f"第{cur_reconnect_tries}次连接失败: {e}")
                time.sleep(1)


    def put_msg(self, new_msg: str):
        self.msg_queue.put(new_msg)
        self._send_pause.set()

    def send_msg(self):
        try:
            while True:
                if self.msg_queue.empty():
                    self._send_pause.clear()
                self._send_pause.wait()

                msg = self.msg_queue.get()
                self.msg_queue.task_done()
                msg_bytes = msg.encode('utf-8')

                # 先发送4字节长度
                self.socket.send(len(msg_bytes).to_bytes(4, 'big'))
                # 再发送实际内容
                self.socket.send(msg_bytes)
        finally:
            self.socket.close()


if __name__ == "__main__":
    client = SocketClient()
    while True:
        msg = input("请输入要发送的数字 (输入 exit 退出): ")
        if msg == 'exit':
            break
        client.put_msg(msg)

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('127.0.0.1', 8888))
# print("已连接到服务器")
#
# while True:
#     msg = input("请输入要发送的字符串 (输入 exit 退出): ")
#     if msg == 'exit':
#         break
#
#     msg_bytes = msg.encode('utf-8')
#
#     # 先发送4字节长度
#     client.send(len(msg_bytes).to_bytes(4, 'big'))  # big 或 little 都要和服务器一致
#     # 再发送实际内容
#     client.send(msg_bytes)
#
#     # 接收服务器回复
#     length_bytes = client.recv(4)
#     length = int.from_bytes(length_bytes, 'big')
#     data = b''
#     while len(data) < length:
#         packet = client.recv(length - len(data))
#         if not packet:
#             break
#         data += packet
#
#     reply = data.decode('utf-8')
#     print(f"服务器回复: {reply}")
#
# client.close()
