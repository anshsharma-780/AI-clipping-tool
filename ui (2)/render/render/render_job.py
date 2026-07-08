from dataclasses import dataclass


@dataclass
class RenderJob:

    input_video: str

    output_video: str

    clip_start: float

    clip_end: float

    crop: dict | None = None

    subtitles: str | None = None

    logo: str | None = None

    logo_position: str = "top-right"