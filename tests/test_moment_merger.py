from ai.highlights.moment_merger import merge_moments

clips = [

    {
        "score": 80,
        "start": 20,
        "end": 30,
        "text": "First clip."
    },

    {
        "score": 90,
        "start": 32,
        "end": 42,
        "text": "Second clip."
    },

    {
        "score": 70,
        "start": 70,
        "end": 80,
        "text": "Third clip."
    }

]

merged = merge_moments(clips)

print("=" * 60)
print("MERGED MOMENTS")
print("=" * 60)

for clip in merged:

    print()

    print(clip)