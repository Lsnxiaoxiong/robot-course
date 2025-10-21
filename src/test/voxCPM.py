import soundfile as sf
import numpy as np
from voxcpm import VoxCPM

model = VoxCPM.from_pretrained("openbmb/VoxCPM-0.5B")

# Non-streaming
wav = model.generate(
    text="以为上了书的就是对的，", # prompt_wav_path="example.wav",  # optional: path to a prompt speech for voice cloning
    # prompt_text="reference transcript",
    cfg_value=2.4,             # LM guidance on LocDiT, higher for better adherence to the prompt, but maybe worse
    inference_timesteps=10,   # LocDiT inference timesteps, higher for better result, lower for fast speed
    normalize=True,           # enable external TN tool
    denoise=False,             # enable external Denoise tool
    retry_badcase=True,        # enable retrying mode for some bad cases (unstoppable)
    retry_badcase_max_times=1,  # maximum retrying times
    retry_badcase_ratio_threshold=6.0, # maximum length restriction for bad case detection (simple but effective), it could be adjusted for slow pace speech
)

sf.write("output.wav", wav, 16000)
print("saved: output.wav")

# Streaming
# chunks = []
# for chunk in model.generate_streaming(
#     text = " 你好，今天天气怎么样？",
#             # prompt_wav_path="skk.wav",      # optional: path to a prompt speech for voice cloning
#             # prompt_text="reference transcript",          # optional: reference text
#             cfg_value=2.0,             # LM guidance on LocDiT, higher for better adherence to the prompt, but maybe worse
#             inference_timesteps=10,   # LocDiT inference timesteps, higher for better result, lower for fast speed
#             normalize=True,           # enable external TN tool
#             denoise=True,             # enable external Denoise tool
#             retry_badcase=False,        # enable retrying mode for some bad cases (unstoppable)
#             retry_badcase_max_times=3,  # maximum retrying times
#             retry_badcase_ratio_threshold=6.0,
# ):
#     chunks.append(chunk)
# wav = np.concatenate(chunks)
#
# sf.write("output_streaming.wav", wav, 16000)
# print("saved: output_streaming.wav")