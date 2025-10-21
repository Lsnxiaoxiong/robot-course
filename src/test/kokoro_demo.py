import os
import queue
import threading

from kokoro import KPipeline, KModel
from IPython.display import display, Audio
import soundfile as sf
import sounddevice as sd
import torch

# 强制离线
# os.environ["HF_HUB_OFFLINE"] = "1"
config_path = "../../model/kokoro82m/config.json"
model_path = "../../model/kokoro82m/kokoro-v1_0.pth"
kmodel = KModel(config=config_path, model=model_path)

# 指定模型目录
# model_dir = r"D:\huggingface\hub\models--hexgrad--Kokoro-82M\snapshots\f3ff3571791e39611d31c381e3a41a3af07b4987"

pipeline = KPipeline(lang_code='z',device='cpu')
# text = '''
# [Kokoro](/kˈOkəɹO/) is an open-weight TTS model with 82 million parameters. Despite its lightweight architecture, it delivers comparable quality to larger models while being significantly faster and more cost-efficient. With Apache-licensed weights, [Kokoro](/kˈOkəɹO/) can be deployed anywhere from production environments to personal projects.
# '''
# text="以为上了书的就是对的，文化落后的中国农民至今还存着这种心理。不谓共产党内讨论问题，也还有人开口闭口“拿本本来”。我们说上级领导机关的指示是正确的，决不单是因为它出于“上级领导机关”，而是因为它的内容是适合于斗争中客观和主观情势的，是斗争所需要的。不根据实际情况进行讨论和审察，一味盲目执行，这种单纯建立在“上级”观念上的形式主义的态度是很不对的。为什么党的策略路线总是不能深入群众，就是这种形式主义在那里作怪。盲目地表面上完全无异议地执行上级的指示，这不是真正在执行上级的指示，这是反对上级指示或者对上级指示怠工的最妙方法。"

text = """
你对于某个问题没有调查，就停止你对于某个问题的发言权。这不太野蛮了吗？一点也不野蛮。你对那个问题的现实情况和历史情况既然没有调查，不知底里，对于那个问题的发言便一定是瞎说一顿。
"""
generator = pipeline(
    text, voice='zf_xiaoxiao',model=kmodel,
    speed=0.95, split_pattern=r'[。！？,\.\!\?、\n]+'
)

# 播放队列
audio_queue = queue.Queue()

def player_worker(rate=16000):
    """持续从队列中读取并顺序播放音频"""
    while True:
        i, audio = audio_queue.get()  # 阻塞等待音频
        if audio is None:
            break  # 结束信号
        print(f"▶ 正在播放第 {i} 段...")
        sd.play(audio, rate)
        sd.wait()  # 等待当前段播放完再继续
        sf.write(f'{i}.wav', audio, rate)
        audio_queue.task_done()

# 启动独立播放线程
player_thread = threading.Thread(target=player_worker, daemon=True)
player_thread.start()

# 主循环：生成并投递音频
for i, (gs, ps, audio) in enumerate(generator):
    print(f"生成第 {i} 段: {gs} / {ps}")
    audio_queue.put((i, audio))  # 放入播放队列

# 所有任务放入后，等待播放完成
audio_queue.join()
audio_queue.put((None, None))  # 结束播放线程
print("✅ 所有音频播放完成。")
