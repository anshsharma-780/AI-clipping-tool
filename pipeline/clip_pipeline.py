from pathlib import Path

from utils.audio_utils import extract_audio
from ai.whisper.transcriber import transcribe_audio
from pipeline.highlight_pipeline import generate_highlights
from ai.highlights.clip_generator import generate_clip


def run_clip_pipeline(video_path, output_folder):
    """
    Complete AI clipping pipeline.

    Steps:
        1. Extract audio
        2. Transcribe audio
        3. Generate AI highlights
        4. Generate video clips

    Returns:
        List of generated clip paths
    """

    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    # ---------------------------------
    # STEP 1
    # Extract Audio
    # ---------------------------------

    print("[1/4] Extracting audio...")

    audio_path = extract_audio(video_path)

    # ---------------------------------
    # STEP 2
    # Whisper
    # ---------------------------------

    print("[2/4] Transcribing audio...")

    transcript = transcribe_audio(audio_path)

    segments_path = transcript["segments"]

    # ---------------------------------
    # STEP 3
    # AI Highlight Detection
    # ---------------------------------

    print("[3/4] Detecting highlights...")

    clips = generate_highlights(
        segments_path
    )

    # ---------------------------------
    # STEP 4
    # Generate MP4 Clips
    # ---------------------------------

    print("[4/4] Generating clips...")

    generated_files = []

    for index, clip in enumerate(clips, start=1):

        output_path = output_folder / f"clip_{index:03}.mp4"

        generate_clip(
            video_path,
            clip["start"],
            clip["end"],
            str(output_path)
        )

        generated_files.append(str(output_path))

    print("Pipeline Complete.")

    return generated_files