import os
import subprocess
import math
from openai import OpenAI
import os
api_key = os.getenv("OPENAI_API_KEY")

def get_file_size(file_path):
    """Get the file size in bytes."""
    return os.path.getsize(file_path)

def get_audio_duration(file_path):
    """Get the duration of the audio file in seconds using ffmpeg."""
    result = subprocess.run(
        ['ffmpeg', '-i', file_path, '-hide_banner'],
        stderr=subprocess.PIPE,
        universal_newlines=True
    )
    for line in result.stderr.split('\n'):
        if 'Duration' in line:
            duration = line.split(',')[0].split('Duration:')[1].strip()
            hours, minutes, seconds = map(float, duration.split(':'))
            return hours * 3600 + minutes * 60 + seconds

def split_audio(file_path, max_size_mb=25):
    # Convert max size from MB to bytes
    max_size_bytes = max_size_mb * 1024 * 1024

    # Get the total size and duration of the audio file
    total_size_bytes = get_file_size(file_path)
    total_duration = get_audio_duration(file_path)

    # Calculate the number of chunks needed
    num_chunks = math.ceil(total_size_bytes / max_size_bytes)

    # Calculate the duration of each chunk in seconds
    chunk_duration = total_duration / num_chunks

    # Get the base filename without extension
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    file_dir = os.path.dirname(file_path)

    # Split and export the chunks
    for i in range(num_chunks):
        start_time = i * chunk_duration
        chunk_filename = f"{base_name}_chunk{i + 1}.m4a"
        chunk_path = os.path.join(file_dir, chunk_filename)

        # Use ffmpeg to split the audio
        subprocess.run([
            'ffmpeg', '-i', file_path, '-ss', str(start_time), '-t', str(chunk_duration),
            '-c', 'copy', chunk_path
        ])

        print(f"Exported {chunk_path}")


# Assuming you have a function `transcribe_audio` that takes a file path and returns the transcript
def transcribe_audio(audio_file):
    client = OpenAI(api_key=api_key)
    # audio_file = open(file_path, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )
    return transcription

