from ai.features.structure_features import structure_score

examples = [

    "THIS is AMAZING!",

    "Do you know the secret?",

    "I earned 1000 dollars today!",

    "Hello everyone.",

    "This is the BEST AI tool ever!"
]

print("=" * 60)
print("STRUCTURE FEATURE TEST")
print("=" * 60)

for sentence in examples:

    result = structure_score(sentence)

    print()
    print(sentence)
    print(result)