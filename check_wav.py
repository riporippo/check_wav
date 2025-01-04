import soundfile as sf
import numpy as np
import wave
filename = 'CRUSHER_SHiMADA.wav' # ファイルの名前

try:
    with sf.SoundFile(filename) as f:
        format_info = f.format
        sample_rate = f.samplerate
        channels = f.channels
    
    with wave.open(filename, 'rb') as wav:
        n_channels = wav.getnchannels()
        sampwidth = wav.getsampwidth()
        framerate = wav.getframerate()
        n_frames = wav.getnframes()
        bit_depth = sampwidth * 8
    
    data, _ = sf.read(filename, dtype='float32', always_2d=True)
    is_clipping = np.any(np.abs(data) >= 1.0)

    print(f"ファイル形式: {format_info}")
    print(f"ビット深度: {bit_depth}-bit")
    print(f"サンプリング周波数 {sample_rate} Hz")
    print(f"Channels: {channels}")
    print(f"メタデータ: channels: {n_channels}, Sample Width: {sampwidth} bytes, Frame Rate: {framerate} Hz, Total Frames: {n_frames}")
    print(f"Clipping: Yes" if is_clipping else "Clipping: No")

except Exception as e:
    print(f"読み込みエラー: {e}")