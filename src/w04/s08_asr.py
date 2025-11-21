import socket
import threading
import time
import queue

import numpy as np
import sounddevice as sd

from src.w04.s05_funasr import SpeechRecognizer



AUDIO_QUEUE = queue.Queue(maxsize=20)

def send_audio_client( server_ip):
    """音频发送客户端：连接到服务器，录音并发送"""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, 50007))
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

def asr():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 50007))
    server.listen(1)
    print(f"接收服务端启动，等待连接...")
    conn, addr = server.accept()
    print(f"客户端已连接: {addr}")

    recognizer = SpeechRecognizer()
    try:
        while True:
            # print("等待录音...")
            data = conn.recv(19200)  # int16 = 2 bytes
            audio_chunk = np.frombuffer(data, dtype=np.int16)
            print("=====>",len(audio_chunk))
            recognizer.start_reco_with_audio(audio_chunk)
            if not data:
                break
    except Exception as e:
        print("接收服务端断开:", e)
    finally:
        conn.close()
        server.close()


if __name__ == "__main__":
    threading.Thread(target=asr).start()
    # asr()
    # time.sleep(1)
    # send_audio_client("localhost")