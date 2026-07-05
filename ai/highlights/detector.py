from ai.highlights.segment_reader import load_segments
from ai.highlights.scorer import score_sentence


def detect_highlights(segments_path, top_n=10):
    """
    Score Whisper segments and return the best candidates.
    """

    segments = load_segments(segments_path)

    candidates = []

    for segment in segments:

        score = score_sentence(segment["text"])

        candidates.append(
            {
                "score": score,
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"]
            }
        )

    candidates.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return candidates[:top_n]