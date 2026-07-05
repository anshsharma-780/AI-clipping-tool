from pipeline.clip_pipeline import run_clip_pipeline

video = input("Enter full video path:\n")

clips = run_clip_pipeline(
    video,
    "processing/clips"
)

print()

print("Generated Clips")

print("----------------------------")

for clip in clips:
    print(clip)