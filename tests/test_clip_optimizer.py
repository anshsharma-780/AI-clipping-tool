from ai.highlights.clip_optimizer import optimize_clip


clips = [

    {
        "score": 90,
        "start": -2,
        "end": 4,
        "text": "Negative start"
    },

    {
        "score": 80,
        "start": 20,
        "end": 25,
        "text": "Very short clip"
    },

    {
        "score": 75,
        "start": 40,
        "end": 120,
        "text": "Very long clip"
    }

]

print("=" * 60)
print("CLIP OPTIMIZER TEST")
print("=" * 60)

for clip in clips:

    optimized = optimize_clip(clip)

    print()
    print("Original")
    print(clip)

    print()

    print("Optimized")
    print(optimized)

    print("-" * 60)