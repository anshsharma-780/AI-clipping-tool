import os
import subprocess


class AudioExtractionError(Exception):
    """Raised when audio extraction fails."""
    pass


def extract_audio(video_path, output_folder="processing/audio"):
    """
    Extract audio from a video using FFmpeg.

    Args:
        video_path (str): Path to input video.
        output_folder (str): Folder where audio.wav will be saved.

    Returns:
        str: Full path to extracted WAV file.
    """

    if not os.path.exists(video_path):
        raise AudioExtractionError(
            f"Video not found:\n{video_path}"
        )

    os.makedirs(output_folder, exist_ok=True)

    output_audio = os.path.join(output_folder, "audio.wav")

    # Remove old file if it exists
    if os.path.exists(output_audio):
        os.remove(output_audio)

    command = [
        "ffmpeg",
        "-y",
        "-i", video_path,
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        output_audio
    ]

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        raise AudioExtractionError(result.stderr)

    return output_audio