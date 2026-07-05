from ai.highlights.keywords import HIGHLIGHT_KEYWORDS


def keyword_score(text: str):
    """
    Calculate keyword-based score.
    """

    score = 0
    matches = []

    import re

    words = re.findall(r"\b[\w']+\b", text.lower())

    for keyword in HIGHLIGHT_KEYWORDS:

        if " " in keyword:
            if keyword.lower() in text.lower():
                score += 10
                matches.append(keyword)

        else:
            if keyword.lower() in words:
                score += 10
                matches.append(keyword)

    return {
        "score": score,
        "matches": matches
    }