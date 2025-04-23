import ffmpeg


input_file = "audios/audio_20250423211547.wav"
output_file = "audios/audio_20250423211547(20).wav"

stream = ffmpeg.input(input_file, ss='00:00:00', t=20)

(
    stream
    .output(output_file, acodec="pcm_s16le", ar=16000)
    .run(overwrite_output=True)
)