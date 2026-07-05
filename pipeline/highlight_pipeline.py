from ai.highlights.segment_reader import load_segments
from ai.highlights.moment_builder import build_moments
from ai.features.feature_engine import extract_features
from ai.highlights.context_optimizer import add_context
from ai.highlights.moment_merger import merge_moments
from ai.highlights.clip_optimizer import optimize_clip

from config import TOP_CLIPS


def generate_highlights(segments_path):
    """
    Complete AI highlight generation pipeline.
    """

    # -----------------------------------
    # Load Whisper Segments
    # -----------------------------------

    segments = load_segments(segments_path)

    # -----------------------------------
    # Build conversational moments
    # -----------------------------------

    moments = build_moments(segments)

    candidates = []

    # -----------------------------------
    # Score every moment
    # -----------------------------------

    for moment in moments:

        text = " ".join(
            segment["text"]
            for segment in moment["segments"]
        )

        features = extract_features(text)

        candidate = {

            "score": features["total_score"],

            "start": moment["start"],

            "end": moment["end"],

            "text": text,

            "features": features

        }

        candidate = add_context(candidate)

        candidate = optimize_clip(candidate)

        candidates.append(candidate)

    # -----------------------------------
    # Merge nearby clips
    # -----------------------------------

    candidates = merge_moments(candidates)

    # -----------------------------------
    # Sort by AI score
    # -----------------------------------

    candidates.sort(
        key=lambda c: c["score"],
        reverse=True
    )

    return candidates[:TOP_CLIPS]