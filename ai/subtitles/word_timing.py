def split_segment_into_words(segment):
    """
    Split a Whisper segment into words with estimated timings.
    """

    text = segment["text"].strip()

    words = text.split()

    if not words:
        return []

    start = segment["start"]
    end = segment["end"]

    duration = end - start

    word_duration = duration / len(words)

    result = []

    current = start

    for word in words:

        result.append(
            {
                "word": word,
                "start": current,
                "end": current + word_duration,
            }
        )

        current += word_duration

    return result