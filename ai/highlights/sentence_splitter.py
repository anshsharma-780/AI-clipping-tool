import re


def split_transcript(transcript: str):
    """
    Split transcript into individual sentences.
    """

    transcript = transcript.replace("\n", " ")

    sentences = re.split(r'(?<=[.!?])\s+', transcript)

    return [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]