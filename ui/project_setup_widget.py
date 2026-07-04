from utils.video_utils import get_video_info
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QFileDialog,
)


class FileSelectorCard(QFrame):
    def __init__(self, title, placeholder, button_text):
        super().__init__()

        self.path = ""

        self.setStyleSheet("""
            QFrame{
                background:#353535;
                border-radius:10px;
            }
        """)

        layout = QVBoxLayout(self)

        title_label = QLabel(title)

        title_label.setStyleSheet("""
            color:white;
            font-size:16px;
            font-weight:bold;
        """)

        layout.addWidget(title_label)

        row = QHBoxLayout()

        self.path_label = QLabel(placeholder)

        self.path_label.setStyleSheet("""
            background:#242424;
            color:#bbbbbb;
            padding:8px;
            border-radius:6px;
        """)

        self.button = QPushButton(button_text)

        self.button.setMinimumWidth(130)

        self.button.setStyleSheet("""
            QPushButton{
                background:#0078D4;
                color:white;
                border:none;
                border-radius:6px;
                padding:8px 15px;
            }

            QPushButton:hover{
                background:#2093ff;
            }
        """)

        row.addWidget(self.path_label)
        row.addWidget(self.button)

        layout.addLayout(row)

    def set_path(self, file_path):

        self.path = file_path

        self.path_label.setText(
            Path(file_path).name
        )

class ProjectSetupWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.build_ui()

    def build_ui(self):

        root = QVBoxLayout(self)

        root.setContentsMargins(40, 30, 40, 30)
        root.setSpacing(20)

        title = QLabel("🚀 New AI Clipping Project")

        title.setStyleSheet("""
            color:white;
            font-size:24px;
            font-weight:bold;
        """)

        root.addWidget(title)

        # -------------------------
        # File Selection Cards
        # -------------------------

        self.video_card = FileSelectorCard(
            "🎥 Input Video",
            "No video selected",
            "Browse Video"
        )

        self.logo_card = FileSelectorCard(
            "🖼 Channel Logo",
            "No logo selected",
            "Browse Logo"
        )

        self.output_card = FileSelectorCard(
            "📂 Output Folder",
            "No output folder selected",
            "Browse Folder"
        )

        root.addWidget(self.video_card)
        root.addWidget(self.logo_card)
        root.addWidget(self.output_card)
        
        # -------------------------
        # Video Information
        # -------------------------

        info = QFrame()

        info.setStyleSheet("""
            QFrame{
                background:#353535;
                border-radius:10px;
            }
        """)

        info_layout = QVBoxLayout(info)

        heading = QLabel("📊 Video Information")

        heading.setStyleSheet("""
            color:white;
            font-size:18px;
            font-weight:bold;
        """)

        info_layout.addWidget(heading)

        self.duration = QLabel("Duration : --")
        self.resolution = QLabel("Resolution : --")
        self.fps = QLabel("FPS : --")
        self.size = QLabel("File Size : --")

        for label in (
            self.duration,
            self.resolution,
            self.fps,
            self.size
        ):
            label.setStyleSheet("color:#cccccc;")
            info_layout.addWidget(label)

        root.addWidget(info)

        self.generate_button = QPushButton("▶ Generate AI Clips")

        self.generate_button.setMinimumHeight(50)

        self.generate_button.setStyleSheet("""
            QPushButton{
                background:#0078D4;
                color:white;
                border:none;
                border-radius:8px;
                font-size:15px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#2093ff;
            }
        """)

        root.addWidget(self.generate_button)

        self.connect_signals()

        root.addStretch()

    def connect_signals(self):
        """Connect all button signals."""

        self.video_card.button.clicked.connect(self.browse_video)

    def browse_video(self):
        """Open file dialog to select a video."""

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Video",
            "",
            "Video Files (*.mp4 *.mov *.avi *.mkv *.wmv)"
        )

        if not file_path:
            return

        # Show selected file name
        self.video_card.set_path(file_path)

        # Read video information
        info = get_video_info(file_path)
        print("Video Info:", info)
        if info is None:
            return

        # Update UI
        self.duration.setText(f"Duration : {info['duration']}")
        self.resolution.setText(f"Resolution : {info['resolution']}")
        self.fps.setText(f"FPS : {info['fps']}")
        self.size.setText(f"File Size : {info['size']}")