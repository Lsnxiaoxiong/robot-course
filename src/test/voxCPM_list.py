import soundfile as sf
import numpy as np
from voxcpm import VoxCPM

import sounddevice as sd



if __name__ == '__main__':
    model = VoxCPM.from_pretrained("openbmb/VoxCPM-0.5B")

    text_list = ['以为上了书的就是对的', '文化落后的中国农民至今还存着这种心理', '不谓共产党内讨论问题',
                 '也还有人开口闭口“拿本本来”', '我们说上级领导机关的指示是正确的', '决不单是因为它出于“上级领导机关”',
                 '而是因为它的内容是适合于斗争中客观和主观情势的', '是斗争所需要的', '不根据实际情况进行讨论和审察',
                 '一味盲目执行', '这种单纯建立在“上级”观念上的形式主义的态度是很不对的',
                 '为什么党的策略路线总是不能深入群众', '就是这种形式主义在那里作怪',
                 '盲目地表面上完全无异议地执行上级的指示', '这不是真正在执行上级的指示',
                 '这是反对上级指示或者对上级指示怠工的最妙方法']

    for text in text_list:
        wav = model.generate(
            text=text,
            # prompt_wav_path="example.wav",  # optional: path to a prompt speech for voice cloning
            # prompt_text="reference transcript",
            cfg_value=2.4,  # LM guidance on LocDiT, higher for better adherence to the prompt, but maybe worse
            inference_timesteps=10,  # LocDiT inference timesteps, higher for better result, lower for fast speed
            normalize=True,  # enable external TN tool
            denoise=False,  # enable external Denoise tool
            retry_badcase=True,  # enable retrying mode for some bad cases (unstoppable)
            retry_badcase_max_times=1,  # maximum retrying times
            retry_badcase_ratio_threshold=6.0,
            # maximum length restriction for bad case detection (simple but effective), it could be adjusted for slow pace speech
        )
        sd.play(wav, samplerate=16000, blocking=False)

    # sf.write("output.wav", wav, 16000)
    print("saved: output.wav")
