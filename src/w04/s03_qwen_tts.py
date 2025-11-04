#  DashScope SDK 版本不低于 1.24.6
# coding=utf-8
#
# Installation instructions for pyaudio:
# APPLE Mac OS X
#   brew install portaudio
#   pip install pyaudio
# Debian/Ubuntu
#   sudo apt-get install python-pyaudio python3-pyaudio
#   or
#   pip install pyaudio
# CentOS
#   sudo yum install -y portaudio portaudio-devel && pip install pyaudio
# Microsoft Windows
#   python -m pip install pyaudio

import os
import dashscope
import pyaudio
import time
import base64
import numpy as np

p = pyaudio.PyAudio()
# 创建音频流
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=24000,
                output=True)


text = "你好啊，我是通义千问"
response = dashscope.MultiModalConversation.call(
    api_key="sk-eebe8334fc4f4c8f82294c16d3f767cf",
    model="qwen3-tts-flash",
    text=text,
    voice="Cherry",
    language_type="Chinese",  # 建议与文本语种一致，以获得正确的发音和自然的语调。
    stream=True
)

for chunk in response:
    audio = chunk.output.audio
    if audio.data is not None:
        wav_bytes = base64.b64decode(audio.data)
        audio_np = np.frombuffer(wav_bytes, dtype=np.int16)
        # 直接播放音频数据
        stream.write(audio_np.tobytes())
    if chunk.output.finish_reason == "stop":
        print("finish at: {} ", chunk.output.audio.expires_at)
time.sleep(0.8)
# 清理资源
stream.stop_stream()
stream.close()
p.terminate()
