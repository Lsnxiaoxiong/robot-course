import socket
import threading
import queue
import time
from typing import Optional

import numpy as np

from src.w04.s06_kokoro import AudioGenerator


class TTSServer:
    """
    TTS服务器类
    封装socket服务器，接收文本并分发合成的音频数据
    """

    def __init__(self, host: str = '0.0.0.0', port: int = 50008):
        """
        初始化TTS服务器

        Args:
            host (str): 服务器监听地址
            port (int): 服务器监听端口
        """
        self.host = host
        self.port = port
        self.text_queue = queue.Queue()
        self.audio_queue = queue.Queue()

        self.socket = None
        self.conn = None

        self.tts = AudioGenerator()
        self.tts.start_generate()

        threading.Thread(target=self._server_worker ).start()
        threading.Thread(target=self._tts_worker).start()


    def _tts_worker(self):
        while True:
            if self.text_queue.empty():
                time.sleep(0.3)
                continue
            text = self.text_queue.get()
            if  text is None or len(text) == 0 or text == '':
                continue
            self.tts.push_text(text)

    def put_text(self, text: str):
        self.text_queue.put(text)

    def _audio_sender(self):
        """音频发送线程，将合成的音频数据发送给客户端"""
        for audio_chunk in self.tts.get_audio():
            if audio_chunk is None:
                continue
            self.conn.sendall(audio_chunk.numpy().tobytes())

    def _server_worker(self):
        """服务器工作线程，处理客户端连接"""

        while True:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((self.host, self.port))
            self.socket.listen(1)
            print(f"TTS服务器启动，等待连接...")
            try:
                self.conn, addr = self.socket.accept()
                print(f"客户端已连接: {addr}")
                thread_audio_sender = threading.Thread(target=self._audio_sender)
                thread_audio_sender.start()

                thread_audio_sender.join()
            except:
                print("连接断开")
            finally:
                self.conn.close()
                self.socket.close()


if __name__ == "__main__":
    tts_server = TTSServer()

    while True:
        text = input("请输入要转换的文本：")
        if text == 'exit':
            break
        tts_server.text_queue.put(text)
