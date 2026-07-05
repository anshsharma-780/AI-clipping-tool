from config import CONTEXT_BEFORE, CONTEXT_AFTER


def add_context(candidate):
    """
    Expand a clip by adding context before and after.
    """

    candidate = candidate.copy()

    candidate["start"] = max(
        0,
        candidate["start"] - CONTEXT_BEFORE
    )

    candidate["end"] += CONTEXT_AFTER

    candidate["duration"] = (
        candidate["end"] - candidate["start"]
    )

    return candidate