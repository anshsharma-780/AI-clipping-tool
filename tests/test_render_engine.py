from render.render_engine import RenderEngine
from render.render_job import RenderJob

video = input("Video:\n")
logo = input("Logo:\n")

job = RenderJob(

    input_video=video,

    output_video="processing/render/final.mp4",

    clip_start=0,

    clip_end=15,

    crop=None,

    subtitles="processing/transcript/subtitles.ass",

    logo=logo,

)

engine = RenderEngine()

output = engine.render(job)

print()

print("=" * 50)

print("RENDER COMPLETE")

print("=" * 50)

print(output)