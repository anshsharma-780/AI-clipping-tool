from pathlib import Path

from ai.whisper.model_loader import get_model


def transcribe_audio(audio_path, output_folder="processing/transcript"):
    """
    Transcribe audio using Whisper.

    Returns:
        transcript_path
    """

    Path(output_folder).mkdir(parents=True, exist_ok=True)

    model = get_model()
    print("Starting transcription...")

    result = model.transcribe(audio_path)
    print("Transcription finished.")

    transcript = result["text"].strip()
    print("Transcript length:", len(transcript))

    transcript_path = Path(output_folder) / "transcript.txt"

    with open(transcript_path, "w", encoding="utf-8") as file:
        file.write(transcript)

    return str(transcript_path)