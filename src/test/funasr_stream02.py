from datetime import datetime

import numpy as np
import sounddevice as sd
from funasr import AutoModel

# --------------------
# 1. 模型与参数
# --------------------
model = AutoModel(model="paraformer-zh-streaming", device='cpu')

chunk_size = [0, 10, 5]  # 当前块大小 (10帧 = 600ms)
encoder_chunk_look_back = 4  # Encoder 向后看 4 个块
decoder_chunk_look_back = 1  # Decoder 向后看 1 个 Encoder 块

SAMPLE_RATE = 16000
FRAME_LEN = 960  # 60ms = 960 采样点
CHUNK_FRAMES = chunk_size[1]  # 10 帧
chunk_stride = CHUNK_FRAMES * FRAME_LEN  # = 9600 采样点 ≈ 600ms

cache = {}  # 模型缓存（跨块记忆）
stream = sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype="int16", blocksize=chunk_stride)
stream.start()

print("🎙 开始实时识别（Ctrl+C 结束）")

# --------------------
# 2. 实时读取 + 推理
# --------------------
try:
    while True:

        # 读取一块音频（600ms）
        data, overflowed = stream.read(chunk_stride)
        if overflowed:
            print("⚠️ 缓冲区溢出")
        speech_chunk = np.frombuffer(data, dtype=np.int16)

        start_time = datetime.now().timestamp()
        # 推理（流式）
        res = model.generate(
            input=speech_chunk,
            cache=cache,
            is_final=False,
            chunk_size=chunk_size,
            encoder_chunk_look_back=encoder_chunk_look_back,
            decoder_chunk_look_back=decoder_chunk_look_back,
        )
        end_time = datetime.now().timestamp()
        if res[0]['text'] != '':
            print("结果：", res[0]['text'])
        # print(f"✅ 识别结果：{res} 耗时：{end_time - start_time:.2f}s")

        # 输出增量识别结果
        print(res)

except KeyboardInterrupt:
    print("🛑 停止识别")

    # 最后一块 flush（告诉模型结束）
    res = model.generate(
        input=np.array([], dtype=np.int16),
        cache=cache,
        is_final=True,
        chunk_size=chunk_size,
        encoder_chunk_look_back=encoder_chunk_look_back,
        decoder_chunk_look_back=decoder_chunk_look_back,
    )
    print("✅ 最终识别结果：", res)
