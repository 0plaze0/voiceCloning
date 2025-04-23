import numpy as np
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
from scipy.io.wavfile import write as write_wav

# 1. Load the model
model_name = "tts_models/multilingual/multi-dataset/your_tts"
manager = ModelManager()
model_path, config_path, model_item = manager.download_model(model_name)

# 2. Load the synthesizer
synthesizer = Synthesizer(
    tts_checkpoint=model_path,
    tts_config_path=config_path,
    use_cuda=False
)

# 3. Reference voice sample
reference_audio = "audios/audio_20250423215638(10).wav"  # Replace with your own .wav sample

# 4. Text to be spoken
text = "Hello, I can speak like the reference voice!"

# 5. Add language_name to fix the multilingual issue
wav = synthesizer.tts(
    text,
    speaker_wav=reference_audio,
    language_name="en"  # Specify the language
)

# 6. Convert the wav (list) to a numpy array and save
wav_np = np.array(wav)  # Convert the list to a numpy array

write_wav("audios/audio_20250423215638(clone).wav", synthesizer.output_sample_rate, wav_np)

print("✅ Voice cloned and saved as cloned_output.wav")
