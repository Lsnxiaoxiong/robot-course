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

    # 压缩为 JPG
    ret, buffer = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
    data = buffer.tobytes()

    # 先发送长度，再发送数据
    conn.sendall(struct.pack(">I", len(data)) + data)

cap.release()
conn.close()
server_socket.close()
