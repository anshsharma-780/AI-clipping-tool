import json
from pathlib import Path


def load_segments(json_path):
    """
    Load Whisper segments from segments.json.
    """

    path = Path(json_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Segments file not found:\n{json_path}"
        )

    with open(path, "r", encoding="utf-8") as file:
        segments = json.load(file)

    cleaned = []

    for segment in segments:

        cleaned.append(
            {
                "start": float(segment["start"]),
                "end": float(segment["end"]),
                "text": segment["text"].strip()
            }
        )

    return cleaned