from ai.features.feature_engine import extract_features

examples = [

    "This is the biggest mistake beginners make!",

    "Here is the secret nobody tells you.",

    "I absolutely love this AI tool!",

    "Hello everyone.",

    "WARNING! Never do this again."
]

print("=" * 60)
print("FEATURE ENGINE TEST")
print("=" * 60)

for sentence in examples:

    result = extract_features(sentence)

    print()
    print(sentence)
    print()

    print("Total Score:", result["total_score"])
    print()

    print(result)