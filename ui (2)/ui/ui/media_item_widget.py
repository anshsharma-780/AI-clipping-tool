import os
import subprocess
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)


class MediaItemWidget(QWidget):
    videoSelected = Signal(str)

    def __init__(
        self,
        video_path,
        thumbnail_path=None,
        duration="Unknown"
    ):
        super().__init__()

        self.video_path = video_path
        self.thumbnail_path = thumbnail_path
        self.duration = duration

        self.setFixedWidth(360)

        layout = QVBoxLayout(self)

        # -----------------------------
        # Thumbnail
        # -----------------------------

        thumb = QLabel()

        thumb.setFixedSize(320, 180)

        thumb.setAlignment(Qt.AlignCenter)

        thumb.setStyleSheet("""
            background:#1d1d1d;
            border:1px solid #444;
            border-radius:6px;
        """)

        if thumbnail_path and os.path.exists(thumbnail_path):

            pix = QPixmap(thumbnail_path)

            thumb.setPixmap(
                pix.scaled(
                    thumb.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )

        else:

            thumb.setText("No Thumbnail")

        layout.addWidget(thumb)

        # -----------------------------
        # Title
        # -----------------------------

        title = QLabel(
            os.path.basename(video_path)
        )

        title.setWordWrap(True)

        title.setStyleSheet("""
            font-size:15px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        # -----------------------------
        # Info
        # -----------------------------

        size = os.path.getsize(video_path) / (1024 * 1024)

        info = QLabel(
            f"⏱ {duration}     📦 {size:.2f} MB"
        )

        info.setStyleSheet("""
            color:gray;
        """)

        layout.addWidget(info)

        # -----------------------------
        # Buttons
        # -----------------------------

        buttons = QHBoxLayout()

        play = QPushButton("▶ Play")
        folder = QPushButton("📂 Folder")
        delete = QPushButton("🗑 Delete")

        play.clicked.connect(self.play_video)
        folder.clicked.connect(self.open_folder)
        delete.clicked.connect(self.delete_video)

        buttons.addWidget(play)
        buttons.addWidget(folder)
        buttons.addWidget(delete)

        layout.addLayout(buttons)

        self.setStyleSheet("""
            QWidget{
                border:1px solid #444;
                border-radius:10px;
                padding:8px;
            }
        """)

    def play_video(self):

        os.startfile(self.video_path)

    def open_folder(self):

        subprocess.Popen([
            "explorer",
            "/select,",
            self.video_path
        ])

    def delete_video(self):

        try:
            os.remove(self.video_path)
            self.hide()
        except Exception as e:
            print(e)

    def mousePressEvent(self, event):

        self.videoSelected.emit(self.video_path)

        super().mousePressEvent(event)