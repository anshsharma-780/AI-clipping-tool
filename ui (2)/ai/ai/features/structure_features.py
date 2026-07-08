import re


def structure_score(text: str):
    """
    Score based on sentence structure.
    """

    score = 0

    details = {
        "question": False,
        "exclamation": False,
        "word_count": 0,
        "numbers": [],
        "uppercase_words": []
    }

    # ------------------------
    # Question
    # ------------------------

    if "?" in text:
        score += 10
        details["question"] = True

    # ------------------------
    # Exclamation
    # ------------------------

    if "!" in text:
        score += 10
        details["exclamation"] = True

    # ------------------------
    # Word Count
    # ------------------------

    words = text.split()

    details["word_count"] = len(words)

    if 8 <= len(words) <= 25:
        score += 20

    elif len(words) > 25:
        score += 10

    # ------------------------
    # Numbers
    # ------------------------

    numbers = re.findall(r"\d+", text)

    details["numbers"] = numbers

    if numbers:
        score += 10

    # ------------------------
    # UPPERCASE words
    # ------------------------

    uppercase = []

    for word in words:

        clean = word.strip(".,!?")

        if len(clean) >= 2 and clean.isupper():
            uppercase.append(clean)

    details["uppercase_words"] = uppercase

    score += len(uppercase) * 5

    return {
        "score": score,
        "details": details
    }