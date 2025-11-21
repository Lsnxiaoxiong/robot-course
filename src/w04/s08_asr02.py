import queue
import socket
import threading
import time
from datetime import datetime

import sounddevice as sd

import numpy as np

from src.w04.s05_funasr import SpeechRecognizer


def recv_exact(conn, n_bytes):
    buffer = b""
    while len(buffer) < n_bytes:
        packet = conn.recv(n_bytes - len(buffer))  # 每次只申请剩下的字节数
        if not packet:  # 返回 b"" 表示对端关闭
            raise ConnectionError("Socket connection broken")
        buffer += packet
    return buffer

def asr(audio_queue, recognizer):
    while True:
        print(">>>",datetime.now(), len(audio_queue.queue))
        if audio_queue.empty():
            time.sleep(0.3)
        audio_chunk = audio_queue.get()
        recognizer.start_reco_with_audio(audio_chunk)
        audio_queue.task_done()

if __name__ == "__main__":

    while True:
        audio_queue = queue.Queue(maxsize=1000)

        recognizer = SpeechRecognizer()
        threading.Thread(target=asr, args=(audio_queue, recognizer)).start()

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', 50007))
        server.listen(1)
        print(f"接收服务端启动，等待连接...")
        conn, addr = server.accept()
        print(f"客户端已连接: {addr}")

        stream = sd.OutputStream(samplerate=16000, channels=1, dtype="int16",
                                blocksize=9600)
        stream.start()
        try:
            while True:
                # print("等待录音...")
                data = recv_exact(conn, 9600*2)
                audio_chunk = np.frombuffer(data, dtype=np.int16)

                print("=====>",len(audio_chunk))
                audio_queue.put(audio_chunk)

                print("<<<", datetime.now(), len(audio_queue.queue))
                stream.write(audio_chunk)
                if not data:
                    break
        except Exception as e:
            print("接收服务端断开:", e)
        finally:
            conn.close()
            server.close()