import sounddevice as sd
import soundfile as sf

def play_wav_stream(filename):
    with sf.SoundFile(filename) as f:
        with sd.OutputStream(
            samplerate=f.samplerate,
            channels=f.channels,
            dtype='float32'
        ) as stream:
            # 分块读取和播放
            blocksize = 2048
            for block in f.blocks(blocksize=blocksize):
                stream.write(block.astype('float32'))

play_wav_stream('skk.wav')
