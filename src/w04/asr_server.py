import queue
import socket
import threading
import time
from datetime import datetime
from typing import Dict, Optional

import sounddevice as sd
import numpy as np

from src.w04.s05_funasr import SpeechRecognizer


class ASRServer:
    """
    ASR服务器类
    封装socket服务器，接收音频数据并进行语音识别
    """

    def __init__(self, host: str = '0.0.0.0', port: int = 50007,
                 audio_output: bool = True, queue_size: int = 1000):
        """
        初始化ASR服务器

        Args:
            host (str): 服务器监听地址
            port (int): 服务器监听端口
            audio_output (bool): 是否播放接收到的音频
            queue_size (int): 音频队列大小
        """
        self.host = host
        self.port = port
        self.audio_output = audio_output
        self.queue_size = queue_size

        # 状态变量
        self._running = False
        self._paused = False
        self._connected = False

        # 组件
        self.audio_queue = queue.Queue(maxsize=queue_size)
        self.recognizer = SpeechRecognizer()
        self.server_socket = None
        self.client_conn = None
        self.audio_stream = None

        # 线程
        self._asr_thread = None
        self._receive_thread = None
        self._server_thread = None

        # 结果存储
        self._recognition_results = {}
        self._latest_result = None

    def start(self):
        """启动ASR服务器"""
        if self._running:
            print("ASR服务器已经在运行中")
            return

        self._running = True
        self._paused = False

        # 启动ASR处理线程
        self._asr_thread = threading.Thread(target=self._asr_worker, daemon=True)
        self._asr_thread.start()

        # 启动服务器线程
        self._server_thread = threading.Thread(target=self._server_worker, daemon=True)
        self._server_thread.start()

        print(f"ASR服务器已启动，监听 {self.host}:{self.port}")

    def stop(self):
        """停止ASR服务器"""
        if not self._running:
            return

        self._running = False
        self._paused = False

        # 关闭连接
        if self.client_conn:
            try:
                self.client_conn.close()
            except:
                pass

        if self.server_socket:
            try:
                self.server_socket.close()
            except:
                pass

        # 停止音频流
        if self.audio_stream:
            try:
                self.audio_stream.stop()
            except:
                pass

        # 清空队列
        self._clear_queue()

        # 等待线程结束
        if self._asr_thread:
            self._asr_thread.join(timeout=2.0)
        if self._server_thread:
            self._server_thread.join(timeout=2.0)
        if self._receive_thread:
            self._receive_thread.join(timeout=2.0)

        print("ASR服务器已停止")

    def pause(self):
        """暂停数据接收"""
        if not self._running:
            print("服务器未运行，无法暂停")
            return

        self._paused = True
        self._clear_queue()
        print("ASR服务器已暂停，队列已清空")

    def resume(self):
        """恢复数据接收"""
        if not self._running:
            print("服务器未运行，无法恢复")
            return

        self._paused = False
        print("ASR服务器已恢复")

    def is_paused(self) -> bool:
        """检查是否处于暂停状态"""
        return self._paused

    def is_connected(self) -> bool:
        """检查是否有客户端连接"""
        return self._connected

    def get_recognition_results(self) -> Dict[float, str]:
        """
        获取所有识别结果

        Returns:
            Dict[float, str]: 时间戳到识别文本的映射
        """
        # 从SpeechRecognizer获取结果
        if hasattr(self.recognizer, 'recognition_res'):
            return self.recognizer.recognition_res.copy()
        return {}

    def get_latest_result(self) -> Optional[str]:
        """
        获取最新的识别结果

        Returns:
            Optional[str]: 最新的识别文本，如果没有则为None
        """
        results = self.get_recognition_results()
        if not results:
            return None

        # 获取最新的时间戳对应的结果
        latest_timestamp = max(results.keys())
        return results[latest_timestamp]

    def _server_worker(self):
        """服务器工作线程，处理客户端连接"""
        while self._running:
            try:
                self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.server_socket.bind((self.host, self.port))
                self.server_socket.listen(1)
                print(f"等待客户端连接...")

                self.client_conn, addr = self.server_socket.accept()
                self._connected = True
                print(f"客户端已连接: {addr}")

                # 启动音频接收线程
                self._receive_thread = threading.Thread(target=self._receive_worker, daemon=True)
                self._receive_thread.start()

                # 等待接收线程结束
                self._receive_thread.join()

                # 连接断开后的清理
                self._connected = False
                if self.audio_stream:
                    self.audio_stream.stop()
                    self.audio_stream = None

                print("客户端连接已断开")

            except Exception as e:
                if self._running:
                    print(f"服务器错误: {e}")
                time.sleep(1)  # 等待后重试

    def _receive_worker(self):
        """音频接收工作线程"""
        try:
            # 初始化音频输出流
            if self.audio_output:
                self.audio_stream = sd.OutputStream(
                    samplerate=16000, channels=1, dtype="int16", blocksize=9600
                )
                self.audio_stream.start()

            while self._running and self._connected:
                # 如果暂停，跳过数据接收
                if self._paused:
                    time.sleep(0.1)
                    continue

                try:
                    # 接收音频数据
                    data = self._recv_exact(self.client_conn, 9600 * 2)
                    if not data:
                        break

                    audio_chunk = np.frombuffer(data, dtype=np.int16)

                    # 放入队列
                    if not self.audio_queue.full():
                        self.audio_queue.put(audio_chunk)
                        # print(f"<<< {datetime.now()} 队列大小: {self.audio_queue.qsize()}")

                    # 播放音频
                    if self.audio_output and self.audio_stream:
                        self.audio_stream.write(audio_chunk)

                except ConnectionError as e:
                    print(f"连接错误: {e}")
                    break
                except Exception as e:
                    print(f"接收错误: {e}")
                    time.sleep(0.1)

        except Exception as e:
            print(f"接收线程错误: {e}")
        finally:
            if self.audio_stream:
                self.audio_stream.stop()
                self.audio_stream = None

    def _asr_worker(self):
        """ASR处理工作线程"""
        while self._running:
            try:
                if self.audio_queue.empty():
                    time.sleep(0.3)
                    continue

                audio_chunk = self.audio_queue.get()
                self.recognizer.start_reco_with_audio(audio_chunk)
                self.audio_queue.task_done()

                # 更新最新结果
                results = self.get_recognition_results()
                if results:
                    latest_timestamp = max(results.keys())
                    self._latest_result = results[latest_timestamp]

            except Exception as e:
                print(f"ASR处理错误: {e}")
                time.sleep(0.1)

    def _recv_exact(self, conn, n_bytes):
        """精确接收指定字节数的数据"""
        buffer = b""
        while len(buffer) < n_bytes:
            packet = conn.recv(n_bytes - len(buffer))
            if not packet:
                raise ConnectionError("Socket连接断开")
            buffer += packet
        return buffer

    def _clear_queue(self):
        """清空音频队列"""
        while not self.audio_queue.empty():
            try:
                self.audio_queue.get_nowait()
                self.audio_queue.task_done()
            except queue.Empty:
                break

    def __enter__(self):
        """上下文管理器入口"""
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器出口"""
        self.stop()


def main():
    """测试函数"""
    # 使用上下文管理器自动管理资源
    with ASRServer(host='0.0.0.0', port=50007, audio_output=True) as server:
        print("ASR服务器运行中...")
        print("命令: pause/resume/status/results/exit")

        try:
            while True:
                cmd = input("> ").strip().lower()

                if cmd == 'pause':
                    server.pause()
                elif cmd == 'resume':
                    server.resume()
                elif cmd == 'status':
                    print(f"运行状态: {'运行中' if server._running else '已停止'}")
                    print(f"暂停状态: {'已暂停' if server.is_paused() else '运行中'}")
                    print(f"连接状态: {'已连接' if server.is_connected() else '未连接'}")
                    print(f"队列大小: {server.audio_queue.qsize()}")
                elif cmd == 'results':
                    results = server.get_recognition_results()
                    if results:
                        print("识别结果:")
                        for timestamp, text in results.items():
                            print(f"  {datetime.fromtimestamp(timestamp)}: {text}")
                    else:
                        print("暂无识别结果")
                elif cmd == 'latest':
                    latest = server.get_latest_result()
                    if latest:
                        print(f"最新结果: {latest}")
                    else:
                        print("暂无最新结果")
                elif cmd == 'exit':
                    break
                else:
                    print("未知命令")

        except KeyboardInterrupt:
            print("\n正在停止服务器...")


if __name__ == "__main__":
    main()