POSITIVE_WORDS = {
    "amazing",
    "awesome",
    "incredible",
    "great",
    "best",
    "love",
    "fantastic",
    "excellent",
    "wow",
    "unbelievable",
    "crazy",
    "insane",
    "viral"
}

NEGATIVE_WORDS = {
    "hate",
    "worst",
    "terrible",
    "awful",
    "problem",
    "mistake",
    "danger",
    "warning",
    "fail",
    "failed"
}


def emotion_score(text: str):
    """
    Estimate emotional intensity using keyword matching.
    """

    score = 0

    positive = []
    negative = []

    words = text.lower().split()

    for word in words:

        clean = word.strip(".,!?")

        if clean in POSITIVE_WORDS:
            positive.append(clean)
            score += 8

        if clean in NEGATIVE_WORDS:
            negative.append(clean)
            score += 8

    return {
        "score": score,
        "details": {
            "positive": positive,
            "negative": negative
        }
    }