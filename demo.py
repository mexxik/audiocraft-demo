import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

model = MusicGen.get_pretrained('facebook/musicgen-melody')
model.set_generation_params(duration=8)
wav = model.generate_unconditional(4)  
descriptions = ['happy rock', 'energetic EDM', 'sad jazz']
wav = model.generate(descriptions)

melody, sr = torchaudio.load('./assets/bach.mp3')
wav = model.generate_with_chroma(descriptions, melody[None].expand(3, -1, -1), sr)

for idx, one_wav in enumerate(wav):
    audio_write(f'./assets/output_{idx}', one_wav.cpu(), model.sample_rate, strategy="loudness", loudness_compressor=True)