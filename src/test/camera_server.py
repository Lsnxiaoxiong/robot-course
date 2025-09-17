import cv2
import socket
import struct
import pickle

def run_server(host="0.0.0.0", port=9999):
    # 打开摄像头
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("无法打开摄像头")
        return

    # 建立TCP服务器
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"等待客户端连接 {host}:{port} ...")

    conn, addr = server_socket.accept()
    print("客户端已连接：", addr)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # 压缩数据（pickle序列化）
            data = pickle.dumps(frame)
            # 先发长度，再发内容
            conn.sendall(struct.pack("!I", len(data)) + data)

    except Exception as e:
        print("异常:", e)
    finally:
        cap.release()
        conn.close()
        server_socket.close()

if __name__ == "__main__":
    run_server()
