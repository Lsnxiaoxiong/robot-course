import sounddevice as sd
import soundfile as sf

# 读取并播放
data, rate = sf.read('skk.wav')
sd.play(data, rate)
sd.wait()  # 等待播放完成