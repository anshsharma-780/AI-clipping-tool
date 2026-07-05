import json
from pathlib import Path

from ai.whisper.model_loader import get_model


def transcribe_audio(audio_path, output_folder="processing/transcript"):
    """
    Transcribe audio using Whisper.

    Returns:
        dict:
        {
            "transcript": "...",
            "segments": "..."
        }
    """

    output_dir = Path(output_folder)
    output_dir.mkdir(parents=True, exist_ok=True)

    model = get_model()

    print("Starting transcription...")

    result = model.transcribe(audio_path)

    print("Transcription finished.")

    transcript = result["text"].strip()
    segments = result["segments"]

    print("Transcript length:", len(transcript))
    print("Segments:", len(segments))

    # -----------------------------
    # Save transcript.txt
    # -----------------------------

    transcript_path = output_dir / "transcript.txt"

    with open(transcript_path, "w", encoding="utf-8") as file:
        file.write(transcript)

    # -----------------------------
    # Save segments.json
    # -----------------------------

    segments_path = output_dir / "segments.json"

    with open(segments_path, "w", encoding="utf-8") as file:
        json.dump(
            segments,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("Transcript saved.")
    print("Segments saved.")

    return {
        "transcript": str(transcript_path),
        "segments": str(segments_path)
    }