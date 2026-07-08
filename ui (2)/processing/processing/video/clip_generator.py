import subprocess
from pathlib import Path


class ClipGenerationError(Exception):
    """Raised when clip generation fails."""
    pass


def generate_clip(
    input_video,
    output_folder,
    start_time,
    end_time,
    output_name="clip_001.mp4"
):
    """
    Generate a video clip using FFmpeg.

    Args:
        input_video (str)
        output_folder (str)
        start_time (float)
        end_time (float)

    Returns:
        str
    """

    output_dir = Path(output_folder)

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path = output_dir / output_name

    duration = end_time - start_time

    command = [
        "ffmpeg",
        "-y",
        "-ss",
        str(start_time),
        "-i",
        input_video,
        "-t",
        str(duration),
        "-c",
        "copy",
        str(output_path)
    ]

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        raise ClipGenerationError(result.stderr)

    return str(output_path)