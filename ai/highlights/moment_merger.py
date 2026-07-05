from config import MERGE_GAP


def merge_moments(candidates):
    """
    Merge nearby clip candidates into larger clips.
    """

    if not candidates:
        return []

    candidates = sorted(
        candidates,
        key=lambda c: c["start"]
    )

    merged = []

    current = candidates[0].copy()

    for candidate in candidates[1:]:

        gap = candidate["start"] - current["end"]

        if gap <= MERGE_GAP:

            current["end"] = max(
                current["end"],
                candidate["end"]
            )

            current["score"] = max(
                current["score"],
                candidate["score"]
            )

            current["text"] += " " + candidate["text"]

        else:

            merged.append(current)

            current = candidate.copy()

    merged.append(current)

    return merged