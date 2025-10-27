import socket
import struct

import cv2
import numpy as np


def get_frame(ip: str="192.168.1.103", port: int=8888):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))

    try:
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

            yield frame
    finally:
        client_socket.close()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    for frame in get_frame():
        cv2.imshow("Client", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break