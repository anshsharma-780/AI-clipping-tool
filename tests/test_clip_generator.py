from processing.video.clip_generator import generate_clip

VIDEO = input("Enter full path of your video:\n")

clip = generate_clip(
    input_video=VIDEO,
    output_folder="processing/clips",
    start_time=0,
    end_time=10
)

print()

print("=" * 40)
print("Clip created successfully")
print("=" * 40)

print(clip)