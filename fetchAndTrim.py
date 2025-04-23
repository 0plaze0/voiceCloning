import sys
import argparse
import pytubefix
import ffmpeg
import time
from datetime import datetime
import os

# Set up argument parsing
parser = argparse.ArgumentParser(description='Download and trim audio from YouTube.')
parser.add_argument('url', help='YouTube video URL')
parser.add_argument('--duration', type=int, default=20, help='Trim duration in seconds (default: 20)')
args = parser.parse_args()

# Create output directory if not exists
os.makedirs("audios", exist_ok=True)

# Generate output file name with timestamp
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
original_filename = f"audios/audio_{timestamp}.wav"
trimmed_filename = f"audios/audio_{timestamp}({args.duration}).wav"

# Download audio from YouTube
print("Downloading audio from YouTube...")
yt = pytubefix.YouTube(args.url)

# Fetch audio stream URL
print("Fetching audio stream...")
stream_url = yt.streams.filter(only_audio=True).first().url

# Convert the stream to .wav format using ffmpeg
print("Converting to .wav format...")
ffmpeg.input(stream_url).output(original_filename, format='wav', loglevel="error").run()

# Save the filename
with open("filename_audio.txt", "w") as text_file:
    text_file.write(original_filename)

print(f"Original audio saved as {original_filename}")

# Trim the audio using user-specified duration
print(f"Trimming the audio to {args.duration} seconds...")
stream = ffmpeg.input(original_filename, ss='00:00:00', t=args.duration)
stream.output(trimmed_filename, acodec="pcm_s16le", ar=16000).run(overwrite_output=True)

print(f"Trimmed audio saved as {trimmed_filename}")
