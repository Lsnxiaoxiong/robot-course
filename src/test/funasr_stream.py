from datetime import datetime

from funasr import AutoModel

chunk_size = [0, 10, 5] # 左上下文块数 当前块包含10帧 右上下文块数 [0, 10, 5] 600ms, [0, 8, 4] 480ms
encoder_chunk_look_back = 4 # 当前块的 Encoder 自注意力机制（self-attention） 不仅看本块的特征，还能向后回看 前4个块的输出。
decoder_chunk_look_back = 1 # 向后看 1 个 encoder 输出块

model = AutoModel(model="paraformer-zh-streaming")

import soundfile
import os

wav_file = os.path.join(model.model_path, "example/asr_example.wav")
speech, sample_rate = soundfile.read(wav_file)
chunk_stride = chunk_size[1] * 960 # 600ms
"""
采样率16kHZ 一帧一般为60ms ，16kHZ*0.06s=960
600ms=10帧  chunk_stride = chunk_size[1] * 960
"""

cache = {}
total_chunk_num = int(len((speech)-1)/chunk_stride+1)
for i in range(total_chunk_num):
    speech_chunk = speech[i*chunk_stride:(i+1)*chunk_stride]
    is_final = i == total_chunk_num - 1

    start_time = datetime.now().timestamp()
    res = model.generate(input=speech_chunk, cache=cache, is_final=is_final, chunk_size=chunk_size,
                         encoder_chunk_look_back=encoder_chunk_look_back,
                         decoder_chunk_look_back=decoder_chunk_look_back )

    end_time = datetime.now().timestamp()
    print(f"✅ 识别结果：{res} 耗时：{end_time - start_time:.2f}s")
    print(res)