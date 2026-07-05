from ai.features.emotion_features import emotion_score

examples = [

    "This is absolutely amazing!",

    "This is the biggest mistake.",

    "I love this AI tool.",

    "That was the worst experience ever.",

    "Hello everyone."
]

print("=" * 60)
print("EMOTION FEATURE TEST")
print("=" * 60)

for sentence in examples:

    print()
    print(sentence)
    print(emotion_score(sentence))