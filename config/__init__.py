"""
Backward compatibility for legacy imports.
"""

from .app_settings import settings

TOP_CLIPS = settings.get("top_clips")

CONTEXT_BEFORE = settings.get("context_before")
CONTEXT_AFTER = settings.get("context_after")

MERGE_GAP = settings.get("merge_gap")

MIN_CLIP_DURATION = settings.get("min_clip_length")
MAX_CLIP_DURATION = settings.get("max_clip_length")

KEYWORD_WEIGHT = settings.get("keyword_weight")
STRUCTURE_WEIGHT = settings.get("structure_weight")
EMOTION_WEIGHT = settings.get("emotion_weight")

WHISPER_MODEL = settings.get("whisper_model")

OUTPUT_FORMAT = settings.get("export_format")