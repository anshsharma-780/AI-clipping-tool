from pipeline.highlight_pipeline import generate_highlights


def detect_highlights(
    segments_path,
    top_n=None
):
    """
    Compatibility wrapper.
    """

    results = generate_highlights(
        segments_path
    )

    if top_n is None:
        return results

    return results[:top_n]