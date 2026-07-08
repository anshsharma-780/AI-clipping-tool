from pathlib import Path

from ai.reframing.smart_reframer import SmartReframer
from render.render_engine import RenderEngine
from render.render_job import RenderJob


def generate_clip(
    video_path,
    start_time,
    end_time,
    output_path,
    subtitle_file=None,
    logo_path=None,
    logo_position="top-right",
):
    """
    Generate a video clip with AI smart 9:16 reframing,
    subtitles and logo overlay.
    """

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    duration = end_time - start_time

    if duration <= 0:
        raise ValueError("Clip duration must be greater than zero.")

    # ------------------------------------
    # AI Smart Reframing
    # ------------------------------------

    reframer = SmartReframer()
    crop = reframer.analyze(video_path)

    # ------------------------------------
    # Render Job
    # ------------------------------------

    job = RenderJob(
        input_video=video_path,
        output_video=str(output),
        clip_start=start_time,
        clip_end=end_time,
        crop=crop,
        subtitles=subtitle_file,
        logo=logo_path,
        logo_position=logo_position,
    )

    engine = RenderEngine()

    return engine.render(job)