import threading
import time
from datetime import datetime

import numpy as np
import sounddevice as sd
from funasr import AutoModel
from joblib.externals.loky.backend.queues import Queue


class SpeechRecognizer:
    def __init__(self, model_dir="paraformer-zh-streaming"):
        model_dir = r"C:\Users\lsn\.cache\modelscope\hub\models\iic\speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-online"
        self.model = AutoModel(
            model=model_dir,
            disable_update=True,
            # device='cpu'

        )
        self.cache = {}
        self.chunk_size = [0, 10, 5]
        self.encoder_chunk_look_back = 4
        self.decoder_chunk_look_back = 1
        self.SAMPLE_RATE = 16000
        self.FRAME_LEN = 960  # 60ms = 960 采样点
        self.CHUNK_FRAMES = self.chunk_size[1]  # 10 帧
        self.chunk_stride = self.CHUNK_FRAMES * self.FRAME_LEN  # = 9600 采样点 ≈ 600ms
        self._pause_event = threading.Event()
        self._pause_event.set()
        self._stop_event = threading.Event()
        self.stream = sd.InputStream(samplerate=self.SAMPLE_RATE, channels=1, dtype="int16",
                                     blocksize=self.chunk_stride)
        self.recognition_res = {}
        self.temp_text = ""
        self.pre_timestamp: float = 0
        self.cur_saving_timestamp = 0

    def recognize(self, speech_chunk):
        # 推理（流式）
        res = self.model.generate(
            input=speech_chunk,
            disable_pbar=True,
            cache=self.cache,
            is_final=False,
            chunk_size=self.chunk_size,
            encoder_chunk_look_back=self.encoder_chunk_look_back,
            decoder_chunk_look_back=self.decoder_chunk_look_back,
        )

        self.save_recognition_res(res)
        # print(f"✅ 识别结果：{res} 耗时：{end_time - start_time:.2f}s")

        # 输出增量识别结果
        # print(res)

    def _generate(self, speech_chunk):
        return self.model.generate(
            input=speech_chunk,
            disable_pbar=True,
            cache=self.cache,
            is_final=False,
            chunk_size=self.chunk_size,
            encoder_chunk_look_back=self.encoder_chunk_look_back,
            decoder_chunk_look_back=self.decoder_chunk_look_back,
        )

    def _generate_final(self):
        return self.model.generate(
            input=np.array([], dtype=np.int16),
            disable_pbar=True,
            cache=self.cache,
            is_final=True,
            chunk_size=self.chunk_size,
            encoder_chunk_look_back=self.encoder_chunk_look_back,
            decoder_chunk_look_back=self.decoder_chunk_look_back,
        )

    def save_recognition_res(self, res):
        interval_time = datetime.now().timestamp() - self.pre_timestamp
        if res[0]['text'] == '':
            if self.pre_timestamp !=0 and interval_time > 1:
                final_res = self._generate_final()
                self.temp_text += final_res[0]['text']
                self.recognition_res[self.cur_saving_timestamp] = self.temp_text
                print(f"保存结果：{self.cur_saving_timestamp} 识别结果：{self.temp_text}")
                self.temp_text = res[0]['text']
                self.pre_timestamp = 0
            return

        if self.pre_timestamp == 0:
            self.pre_timestamp = self.cur_saving_timestamp = datetime.now().timestamp()
            self.temp_text += res[0]['text']
            print(f"{self.pre_timestamp} 开始结果：{self.temp_text}")
        elif interval_time < 1:
            self.temp_text += res[0]['text']
            self.pre_timestamp = datetime.now().timestamp()
            print(f"识别结果：{self.temp_text}")
        # else:
        #     final_res = self._generate_final()
        #     self.temp_text += final_res[0]['text']
        #     self.recognition_res[self.cur_saving_timestamp] = self.temp_text
        #     print(f"保存结果：{self.cur_saving_timestamp} 识别结果：{self.temp_text}")
        #     self.temp_text = res[0]['text']
        #     self.pre_timestamp = 0

    def start_recognition(self):
        self.stream.start()
        while not self._stop_event.is_set():
            self._pause_event.wait()
            data, overflowed = self.stream.read(self.chunk_stride)
            if overflowed:
                print("⚠️ 缓冲区溢出")
            speech_chunk = np.frombuffer(data, dtype=np.int16)
            self.recognize(speech_chunk)

    def start_reco_with_audio(self, audio_chunk: np.ndarray):
        self.recognize(audio_chunk)

    def async_run(self):
        threading.Thread(target=self.start_recognition, daemon=True).start()

    def resume(self):
        self._pause_event.set()

    def pause(self):
        self._pause_event.clear()

    def stop(self):
        self._stop_event.set()
        self._pause_event.set()
        self.stream.stop()
        res = self.model.generate(
            input=np.array([], dtype=np.int16),
            cache=self.cache,
            is_final=True,
            chunk_size=self.chunk_size,
            encoder_chunk_look_back=self.encoder_chunk_look_back,
            decoder_chunk_look_back=self.decoder_chunk_look_back,
        )
        print(f"🛑 最终识别结果：{res}")


if __name__ == "__main__":
    recognizer = SpeechRecognizer()
    recognizer.async_run()
    time.sleep(600)
