import whisper

# Load Whisper model (base = faster, medium = more accurate)
model = whisper.load_model("base")

# Transcribe the audio file with word-level timestamps
result = model.transcribe("squeaky_shrimp_segment.wav", word_timestamps=True)

# Print each word with its start and end time
for segment in result['segments']:
    for word in segment['words']:
        print(f"{word['start']:.2f}s - {word['end']:.2f}s: {word['word'].strip()}")
