import subprocess
from pathlib import Path


def burn_subtitles(
    input_video,
    subtitle_file,
    output_video
):
    """
    Burn ASS subtitles into a video using FFmpeg.
    """

    output = Path(output_video)
    output.parent.mkdir(parents=True, exist_ok=True)

    command = [
        "ffmpeg",
        "-y",
        "-i", input_video,
        "-vf", f"ass={subtitle_file}",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-c:a", "copy",
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