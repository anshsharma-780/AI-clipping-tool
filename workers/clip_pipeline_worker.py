from PySide6.QtCore import QObject, Signal

from pipeline.clip_pipeline import run_clip_pipeline


class ClipPipelineWorker(QObject):
    """
    Runs the complete AI clipping pipeline in a background thread.
    """

    finished = Signal(list)
    error = Signal(str)
    progress = Signal(int, str)

    def run(self, video_path, output_folder, logo_path=None):
        try:

            clips = run_clip_pipeline(
                video_path=video_path,
                output_folder=output_folder,
                progress_callback=self.progress.emit,
                logo_path=logo_path,
            )

            self.finished.emit(clips)

        except Exception as e:

            self.error.emit(str(e))