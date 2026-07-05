from ai.highlights.segment_reader import load_segments
from ai.highlights.moment_builder import build_moments

segments = load_segments(
    "processing/transcript/segments.json"
)

moments = build_moments(segments)

print()

print("=" * 50)
print("MOMENTS")
print("=" * 50)

for i, moment in enumerate(moments, 1):

    print()

    print(f"Moment {i}")

    print(
        f"{moment['start']} -> {moment['end']}"
    )

    print()

    for seg in moment["segments"]:

        print("-", seg["text"])