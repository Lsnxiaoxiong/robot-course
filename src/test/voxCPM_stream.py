import queue
import threading

import soundfile as sf
import numpy as np
import sounddevice as sd
from voxcpm import VoxCPM

model = VoxCPM.from_pretrained("openbmb/VoxCPM-0.5B")

import threading
import queue

q = queue.Queue()
done = threading.Event()


def producer():
    for chunk in model.generate_streaming(
            text="以为上了书的就是对的，文化落后的中国农民至今还存着这种心理。",
            # text="以为上了书的就是对的，文化落后的中国农民至今还存着这种心理。不谓共产党内讨论问题，也还有人开口闭口“拿本本来”。我们说上级领导机关的指示是正确的，决不单是因为它出于“上级领导机关”，而是因为它的内容是适合于斗争中客观和主观情势的，是斗争所需要的。不根据实际情况进行讨论和审察，一味盲目执行，这种单纯建立在“上级”观念上的形式主义的态度是很不对的。为什么党的策略路线总是不能深入群众，就是这种形式主义在那里作怪。盲目地表面上完全无异议地执行上级的指示，这不是真正在执行上级的指示，这是反对上级指示或者对上级指示怠工的最妙方法。",
            cfg_value=2.3,  # LM guidance on LocDiT, higher for better adherence to the prompt, but maybe worse
            inference_timesteps=10,  # LocDiT inference timesteps, higher for better result, lower for fast speed
            normalize=True,  # enable external TN tool
            denoise=False,  # enable external Denoise tool
            retry_badcase=False,  # enable retrying mode for some bad cases (unstoppable)
            retry_badcase_max_times=1,  # maximum retrying times
            retry_badcase_ratio_threshold=6.0,

    ):
        q.put(chunk)
    done.set()  # 生成完成


def consumer():
    # 缓冲 1 秒的音频后开始播放
    buffer_time = 1.0
    buffered = []
    sample_rate = 16000

    # 预先积累一点缓冲
    while not done.is_set() and sum(len(c) for c in buffered) / sample_rate < buffer_time:
        buffered.append(q.get())

    # 开始播放
    stream = sd.OutputStream(samplerate=sample_rate*0.9, channels=1, dtype="float32")
    stream.start()
    for chunk in buffered:
        stream.write(chunk.astype(np.float32))

    while not (done.is_set() and q.empty()):
        chunk = q.get()
        stream.write(chunk.astype(np.float32))

    stream.stop()
    stream.close()



if __name__ == "__main__":
     # 启动线程
     threading.Thread(target=producer).start()
     consumer()