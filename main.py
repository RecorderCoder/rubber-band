from demucs import pretrained
from demucs.apply import apply_model
import torchaudio
import os

# 사용 가능한 백엔드 출력
print("Available backends:", torchaudio.list_audio_backends())

# 파일 경로 확인
file_path = "C:/Python_workspace/rubber-band/sample3/downloaded_audio.wav"
if not os.path.exists(file_path):
    print(f"Error: File {file_path} does not exist.")
    exit(1)

# 모델 로드
model = pretrained.get_model("htdemucs")

# 오디오 로드
waveform, sample_rate = torchaudio.load(file_path)

# 오디오 분리
sources = apply_model(model, waveform[None])[0]

# 분리된 트랙 (보컬, 드럼, 베이스, 기타)
drum, bass, other, vocal = sources

# 트랙 저장
torchaudio.save("vocal.wav", vocal, sample_rate)
torchaudio.save("drum.wav", drum, sample_rate)
torchaudio.save("bass.wav", bass, sample_rate)
torchaudio.save("other.wav", other, sample_rate)