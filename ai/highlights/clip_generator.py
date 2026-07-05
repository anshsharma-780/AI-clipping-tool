import subprocess
from pathlib import Path


import subprocess
from pathlib import Path


def generate_clip(video_path, start_time, end_time, output_path):
    """
    Generate a video clip with audio using FFmpeg.
    """

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    duration = end_time - start_time

    if duration <= 0:
        raise ValueError("Clip duration must be greater than zero.")

    command = [
        "ffmpeg",
        "-y",

        "-i", video_path,

        "-ss", str(start_time),

        "-t", str(duration),

        "-c:v", "libx264",
        "-preset", "fast",
        "-pix_fmt", "yuv420p",

        "-c:a", "aac",
        "-b:a", "192k",

        "-movflags", "+faststart",

        str(output)
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return str(output)