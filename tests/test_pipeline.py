from pipeline.highlight_pipeline import generate_highlights


def format_time(seconds):

    minutes = int(seconds // 60)

    seconds = int(seconds % 60)

    return f"{minutes:02}:{seconds:02}"


clips = generate_highlights(
    "processing/transcript/segments.json"
)

print("=" * 70)
print("FULL AI PIPELINE")
print("=" * 70)

for index, clip in enumerate(clips, 1):

    print()

    print(f"Candidate #{index}")

    print("-" * 40)

    print("Score :", clip["score"])

    print(
        "Time  :",
        format_time(clip["start"]),
        "-",
        format_time(clip["end"])
    )

    print()

    print(clip["text"])