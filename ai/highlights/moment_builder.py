from config import MERGE_GAP

def build_moments(segments, max_gap=MERGE_GAP):
    """
    Merge nearby Whisper segments into
    larger conversational moments.
    """

    if not segments:
        return []

    moments = []

    current = {
        "start": segments[0]["start"],
        "end": segments[0]["end"],
        "segments": [segments[0]]
    }

    for segment in segments[1:]:

        gap = segment["start"] - current["end"]

        if gap <= max_gap:

            current["segments"].append(segment)
            current["end"] = segment["end"]

        else:

            moments.append(current)

            current = {
                "start": segment["start"],
                "end": segment["end"],
                "segments": [segment]
            }

    moments.append(current)

    return moments