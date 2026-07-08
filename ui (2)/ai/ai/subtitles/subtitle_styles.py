# ==========================================================
# Subtitle Theme Engine
# ==========================================================

SUBTITLE_THEMES = {

    "tiktok": {
        "font": "Arial",
        "size": 68,
        "primary": "&H00FFFFFF",
        "secondary": "&H0000FFFF",
        "outline": "&H00000000",
        "back": "&H64000000",
        "bold": -1,
        "italic": 0,
        "outline_width": 4,
        "shadow": 2,
        "alignment": 2,
        "margin_left": 60,
        "margin_right": 60,
        "margin_vertical": 120,
    },

    "instagram": {
        "font": "Arial",
        "size": 58,
        "primary": "&H00FFFFFF",
        "secondary": "&H0000FFFF",
        "outline": "&H00000000",
        "back": "&H50000000",
        "bold": -1,
        "italic": 0,
        "outline_width": 3,
        "shadow": 1,
        "alignment": 2,
        "margin_left": 70,
        "margin_right": 70,
        "margin_vertical": 110,
    },

    "minimal": {
        "font": "Arial",
        "size": 52,
        "primary": "&H00FFFFFF",
        "secondary": "&H00FFFFFF",
        "outline": "&H00000000",
        "back": "&H00000000",
        "bold": 0,
        "italic": 0,
        "outline_width": 2,
        "shadow": 0,
        "alignment": 2,
        "margin_left": 70,
        "margin_right": 70,
        "margin_vertical": 100,
    }

}


def build_style(theme="tiktok"):

    style = SUBTITLE_THEMES.get(theme, SUBTITLE_THEMES["instagram"])

    return (
        "Style: Default,"
        f"{style['font']},"
        f"{style['size']},"
        f"{style['primary']},"
        f"{style['secondary']},"
        f"{style['outline']},"
        f"{style['back']},"
        f"{style['bold']},"
        f"{style['italic']},"
        "0,0,"
        "100,100,"
        "0,0,"
        "1,"
        f"{style['outline_width']},"
        f"{style['shadow']},"
        f"{style['alignment']},"
        f"{style['margin_left']},"
        f"{style['margin_right']},"
        f"{style['margin_vertical']},"
        "1"
    )