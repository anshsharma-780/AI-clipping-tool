"""
Application Default Settings
"""

DEFAULT_SETTINGS = {

    # =====================================
    # AI
    # =====================================

    "top_clips": 5,

    "highlight_threshold": 30,

    "keyword_weight": 1.0,

    "structure_weight": 1.0,

    "emotion_weight": 1.0,

    # =====================================
    # Clip Generation
    # =====================================

    "context_before": 5,

    "context_after": 5,

    "merge_gap": 3,

    "min_clip_length": 15,

    "max_clip_length": 60,

    # =====================================
    # Whisper
    # =====================================

    "whisper_model": "base",

    # =====================================
    # Rendering
    # =====================================

    "output_quality": "high",

    "video_codec": "libx264",

    "preset": "fast",

    "crf": 18,

    # =====================================
    # Subtitle
    # =====================================

    "subtitle_enabled": True,

    "subtitle_theme": "tiktok",

    # =====================================
    # Branding
    # =====================================

    "logo_enabled": True,

    "logo_position": "top-right",

    "logo_scale": 0.12,

    # =====================================
    # Smart Crop
    # =====================================

    "smart_crop": True,

    "crop_ratio": "9:16",

    # =====================================
    # Export
    # =====================================

    "export_format": "mp4",

    "open_output_folder": True,

}