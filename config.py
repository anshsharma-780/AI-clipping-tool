"""
AI Clipping Tool Configuration
"""

# ----------------------------
# AI SETTINGS
# ----------------------------

TOP_CLIPS = 5

# ----------------------------
# CLIP SETTINGS
# ----------------------------

CONTEXT_BEFORE = 5
CONTEXT_AFTER = 5

MERGE_GAP = 3

MIN_CLIP_DURATION = 15
MAX_CLIP_DURATION = 60

# ----------------------------
# FEATURE WEIGHTS
# ----------------------------

KEYWORD_WEIGHT = 1.0
STRUCTURE_WEIGHT = 1.0
EMOTION_WEIGHT = 1.0

# ----------------------------
# WHISPER
# ----------------------------

WHISPER_MODEL = "base"

# ----------------------------
# OUTPUT
# ----------------------------

OUTPUT_FORMAT = "mp4"