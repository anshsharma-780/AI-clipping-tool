from config import (
    MIN_CLIP_DURATION,
    MAX_CLIP_DURATION
)


def optimize_clip(candidate):
    """
    Ensure clip duration is valid and timestamps are safe.
    """

    candidate = candidate.copy()

    # Never allow negative start time
    if candidate["start"] < 0:
        candidate["start"] = 0

    duration = candidate["end"] - candidate["start"]

    # Too short → extend the end
    if duration < MIN_CLIP_DURATION:
        candidate["end"] = candidate["start"] + MIN_CLIP_DURATION

    # Too long → trim the end
    elif duration > MAX_CLIP_DURATION:
        candidate["end"] = candidate["start"] + MAX_CLIP_DURATION

    candidate["duration"] = (
        candidate["end"] - candidate["start"]
    )

    return candidate