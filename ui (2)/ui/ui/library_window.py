import sys

from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
)

from ui.media_library import MediaLibrary
from ui.video_player_widget import VideoPlayerWidget


class LibraryWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Media Library")

        layout = QHBoxLayout(self)

        self.library = MediaLibrary()

        self.player = VideoPlayerWidget()

        layout.addWidget(self.library, 1)

        layout.addWidget(self.player, 2)

        self.library.videoSelected.connect(
            self.player.load_video
        )