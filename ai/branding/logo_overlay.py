import subprocess
from pathlib import Path


def overlay_logo(
    input_video,
    logo_path,
    output_video,
    position="top-right",
    scale=0.12,
):
    """
    Overlay a logo onto a video.

    Parameters
    ----------
    input_video : str
    logo_path : str
    output_video : str
    position : str
        top-right, top-left, bottom-right, bottom-left
    scale : float
        Fraction of video width.
    """

    output = Path(output_video)
    output.parent.mkdir(parents=True, exist_ok=True)

    positions = {
        "top-right": "main_w-overlay_w-30:30",
        "top-left": "30:30",
        "bottom-right": "main_w-overlay_w-30:main_h-overlay_h-30",
        "bottom-left": "30:main_h-overlay_h-30",
    }

    overlay = positions.get(position, positions["top-right"])

    filter_complex = (
        f"[1:v]scale=iw*{scale}:-1[logo];"
        f"[0:v][logo]overlay={overlay}"
    )

    command = [
        "ffmpeg",
        "-y",
        "-i", input_video,
        "-i", logo_path,
        "-filter_complex", filter_complex,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-c:a", "copy",
        str(output),
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return str(output)