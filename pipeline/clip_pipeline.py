from pathlib import Path

from config.app_settings import settings
from utils.audio_utils import extract_audio
from ai.whisper.transcriber import transcribe_audio
from pipeline.highlight_pipeline import generate_highlights
from ai.highlights.clip_generator import generate_clip
from ai.subtitles.ass_generator import generate_ass


def run_clip_pipeline(
    video_path,
    output_folder,
    progress_callback=None,
    logo_path=None,
):
    """
    Complete AI clipping pipeline.

    Parameters
    ----------
    video_path : str

    output_folder : str

    progress_callback : callable, optional

        Function with signature:

            progress_callback(percent, message)

    Returns
    -------
    list
        Generated clip paths.
    """

    output_folder = Path(output_folder)
    output_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    # ============================================
    # STEP 1
    # Extract Audio
    # ============================================

    if progress_callback:
        progress_callback(
            10,
            "Extracting audio..."
        )

    print("[1/4] Extracting audio...")

    audio_path = extract_audio(
        video_path
    )

    # ============================================
    # STEP 2
    # Whisper
    # ============================================

    if progress_callback:
        progress_callback(
            35,
            "Transcribing audio..."
        )

    print("[2/4] Transcribing audio...")

    transcript = transcribe_audio(
        audio_path
    )

    segments_path = transcript["segments"]

    subtitle_file = None
    if settings.get("subtitle_enabled"):
        subtitle_file = output_folder / "subtitles.ass"
        generate_ass(str(segments_path), str(subtitle_file))

    # ============================================
    # STEP 3
    # Highlight Detection
    # ============================================

    if progress_callback:
        progress_callback(
            60,
            "Detecting highlights..."
        )

    print("[3/4] Detecting highlights...")

    clips = generate_highlights(
        segments_path
    )

    # ============================================
    # STEP 4
    # Generate Clips
    # ============================================

    generated_files = []

    total = len(clips)

    if total == 0:

        if progress_callback:
            progress_callback(
                100,
                "No highlights found."
            )

        return generated_files

    for index, clip in enumerate(clips, start=1):

        percent = 75 + int((index / total) * 25)

        if progress_callback:
            progress_callback(
                percent,
                f"Generating clip {index}/{total}..."
            )

        output_path = output_folder / f"clip_{index:03}.mp4"

        generate_clip(
            video_path,
            clip["start"],
            clip["end"],
            str(output_path),
            subtitle_file=str(subtitle_file) if subtitle_file else None,
            logo_path=logo_path,
        )

        generated_files.append(
            str(output_path)
        )

    if progress_callback:
        progress_callback(
            100,
            "Complete!"
        )

    print("Pipeline Complete.")

    return generated_files