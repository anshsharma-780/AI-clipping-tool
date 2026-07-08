import glob
import os

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QScrollArea,
)

from ui.media_item_widget import MediaItemWidget


class MediaLibrary(QWidget):

    videoSelected = Signal(str)

    def __init__(self):

        super().__init__()

        self.main_layout = QVBoxLayout(self)

        title = QLabel("Media Library")

        title.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
        """)

        self.main_layout.addWidget(title)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.main_layout.addWidget(self.scroll)

        self.refresh_library()

    # ====================================================

    def refresh_library(self):

        container = QWidget()

        self.container_layout = QVBoxLayout(container)

        clips = glob.glob(
            os.path.join(
                "processing",
                "clips",
                "*.mp4"
            )
        )

        if not clips:

            empty = QLabel("No clips generated yet.")

            empty.setStyleSheet("""
                color:gray;
                font-size:15px;
            """)

            self.container_layout.addWidget(empty)

        else:

            for clip in clips:

                thumb = clip.replace(".mp4", ".jpg")

                item = MediaItemWidget(
                    clip,
                    thumb
                )

                item.videoSelected.connect(
                    self.videoSelected.emit
                )

                self.container_layout.addWidget(item)

        self.container_layout.addStretch()

        self.scroll.setWidget(container)