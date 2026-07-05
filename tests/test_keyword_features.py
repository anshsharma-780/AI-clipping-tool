from ai.features.keyword_features import keyword_score

examples = [

    "This is the biggest mistake beginners make.",

    "Here is the secret nobody tells you.",

    "Hello everyone.",

    "This is unbelievable!",

    "Today I will show you the best AI tool."
]

print("=" * 60)
print("KEYWORD FEATURE TEST")
print("=" * 60)

for sentence in examples:

    result = keyword_score(sentence)

    print()

    print(sentence)

    print(result)