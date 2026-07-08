from ai.highlights.keywords import HIGHLIGHT_KEYWORDS


def score_sentence(sentence: str):
    """
    Calculate a highlight score for one sentence.
    """

    score = 0

    text = sentence.lower()

    # ------------------------
    # Keyword score
    # ------------------------

    for keyword in HIGHLIGHT_KEYWORDS:

        if keyword.lower() in text:
            score += 10

    # ------------------------
    # Length score
    # ------------------------

    words = len(sentence.split())

    if 8 <= words <= 25:
        score += 20

    elif words > 25:
        score += 10

    # ------------------------
    # Excitement score
    # ------------------------

    score += sentence.count("!") * 5
    score += sentence.count("?") * 3

    return score