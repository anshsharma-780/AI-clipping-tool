from render.render_job import RenderJob
from render.ffmpeg_builder import FFmpegBuilder

job = RenderJob(
    input_video="input.mp4",
    output_video="output.mp4",
    clip_start=10,
    clip_end=25,
    crop={
        "x": 420,
        "y": 0,
        "width": 405,
        "height": 720,
    },
    subtitles="processing/transcript/subtitles.ass",
    logo="logo.png",
)

builder = FFmpegBuilder()

command = builder.build(job)

print()

print("=" * 60)
print("FFMPEG COMMAND")
print("=" * 60)

print()

print(" ".join(command))