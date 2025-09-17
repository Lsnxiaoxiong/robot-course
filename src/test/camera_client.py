import cv2
import socket
import struct
import numpy as np

SERVER_IP = "192.168.1.103"  # 修改为实际IP
PORT = 9999

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, PORT))

    data = b""
    payload_size = struct.calcsize("!I")

    try:
        while True:
            # 先收 4 字节长度
            while len(data) < payload_size:
                packet = client_socket.recv(4096)
                if not packet:
                    return
                data += packet

            packed_size = data[:payload_size]
            data = data[payload_size:]
            frame_size = struct.unpack("!I", packed_size)[0]

            # 收完整帧
            while len(data) < frame_size:
                packet = client_socket.recv(4096)
                if not packet:
                    return
                data += packet

            frame_data = data[:frame_size]
            data = data[frame_size:]

            # 解码 JPEG
            frame = cv2.imdecode(np.frombuffer(frame_data, dtype=np.uint8), cv2.IMREAD_COLOR)

            if frame is not None:
                cv2.imshow("Remote Camera", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
    finally:
        client_socket.close()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    run_client()
