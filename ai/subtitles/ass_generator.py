import json
from config.app_settings import settings
from ai.subtitles.subtitle_styles import build_style


def seconds_to_ass(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60

    return f"{hours}:{minutes:02}:{secs:05.2f}"

def generate_ass(
    segments_json,
    output_file,
    theme=None
):

    if theme is None:
        theme = settings.get("subtitle_theme")

    with open(segments_json, "r", encoding="utf-8") as f:
        segments = json.load(f)

    with open(output_file, "w", encoding="utf-8") as f:

        f.write("[Script Info]\n")
        f.write("ScriptType: v4.00+\n")
        f.write("PlayResX: 1080\n")
        f.write("PlayResY: 1920\n")
        f.write("\n")

        f.write("[V4+ Styles]\n")
        f.write("Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding\n")
        f.write(build_style(theme).strip())
        f.write("\n\n")

        f.write("[Events]\n")
        f.write("Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text\n")

        count = 0

        for segment in segments:

            text = (
                segment["text"]
                .strip()
                .replace("\n", " ")
                .upper()
            )
            while "  " in text:
                text = text.replace("  ", " ")
            if not text:
                continue

            start = seconds_to_ass(segment["start"])
            end = seconds_to_ass(segment["end"])

            f.write(
                f"Dialogue: 0,{start},{end},Default,,0,0,0,,{text}\n"
            )

            count += 1

    print(f"Generated {count} subtitle lines.")