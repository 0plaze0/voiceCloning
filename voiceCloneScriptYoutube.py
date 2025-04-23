import sys
import argparse
import os
from datetime import datetime
import pytubefix
import ffmpeg
import numpy as np
from scipy.io.wavfile import write as write_wav
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

# --- Argument Parsing ---
parser = argparse.ArgumentParser(description="Clone a voice from YouTube or local .wav and speak custom text.")
parser.add_argument('--url', type=str, help="YouTube video URL")
parser.add_argument('--reference', type=str, help="Path to local .wav file (optional, skips download if provided)")
parser.add_argument('--duration', type=int, default=20, help="Trim duration in seconds (default: 20)")
parser.add_argument('--text', type=str, required=True, help="Text to synthesize using cloned voice")
args = parser.parse_args()

# --- Create Output Folder if It Doesn't Exist ---
os.makedirs("audios", exist_ok=True)

# --- Output Setup ---
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
original_filename = f"audios/audio_{timestamp}.wav"
trimmed_filename = f"audios/audio_{timestamp}({args.duration}).wav"
cloned_output = f"audios/audio_{timestamp}(clone).wav"

# --- Download and Trim ---
if args.reference:
    print(f"Using local reference file: {args.reference}")
    reference_audio = args.reference
else:
    if not args.url:
        print(" Either --url or --reference must be provided.")
        sys.exit(1)

    try:
        print(" Downloading audio from YouTube...")
        yt = pytubefix.YouTube(args.url)
        stream_url = yt.streams.filter(only_audio=True).first().url

        print(" Converting to .wav...")
        ffmpeg.input(stream_url).output(original_filename, format='wav', loglevel="error").run()

        print(f" Trimming to {args.duration} seconds...")
        ffmpeg.input(original_filename, ss='00:00:00', t=args.duration) \
              .output(trimmed_filename, acodec="pcm_s16le", ar=16000) \
              .run(overwrite_output=True)

        reference_audio = trimmed_filename
        print(f"Trimmed audio saved as: {reference_audio}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

# --- Voice Cloning ---
print("Loading voice cloning model...")
model_name = "tts_models/multilingual/multi-dataset/your_tts"
manager = ModelManager()
model_path, config_path, _ = manager.download_model(model_name)

synthesizer = Synthesizer(
    tts_checkpoint=model_path,
    tts_config_path=config_path,
    use_cuda=False
)

print("Generating cloned voice...")
try:
    wav = synthesizer.tts(
        args.text,
        speaker_wav=reference_audio,
        language_name="en"
    )
    wav_np = np.array(wav)
    write_wav(cloned_output, synthesizer.output_sample_rate, wav_np)
    print(f"Voice cloned and saved as: {cloned_output}")
except Exception as e:
    print(f" Synthesis failed: {e}")
