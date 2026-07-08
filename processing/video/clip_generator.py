import subprocess
from pathlib import Path

from render.render_engine import RenderEngine
from render.render_job import RenderJob


class ClipGenerationError(Exception):
    """Raised when clip generation fails."""
    pass


def generate_clip(
    input_video,
    output_folder,
    start_time,
    end_time,
    output_name="clip_001.mp4",
    subtitle_file=None,
    logo_path=None,
    logo_position="top-right",
):
    """
    Generate a video clip using the render engine so subtitles and logos
    are preserved in the exported clip.

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

    job = RenderJob(
        input_video=input_video,
        output_video=str(output_path),
        clip_start=start_time,
        clip_end=end_time,
        subtitles=subtitle_file,
        logo=logo_path,
        logo_position=logo_position,
    )

    engine = RenderEngine()
    return engine.render(job)