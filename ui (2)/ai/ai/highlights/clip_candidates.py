from ai.highlights.detector import detect_highlights


def generate_candidates(segments_path):
    """
    Return AI clip candidates.
    """

    return detect_highlights(segments_path)