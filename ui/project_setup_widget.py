import os
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl
from PySide6.QtCore import QThread, Signal

from workers.clip_pipeline_worker import ClipPipelineWorker
from ui.progress_dialog import ProgressDialog
from utils.audio_utils import extract_audio
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
     QMessageBox,
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
    generationFinished = Signal()

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
        self.logo_card.button.clicked.connect(self.browse_logo)
        self.output_card.button.clicked.connect(self.browse_output_folder)
        self.generate_button.clicked.connect(self.generate_project)
        
    def browse_video(self):
        """Select input video."""

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Video",
            "",
            "Videos (*.mp4 *.mov *.avi *.mkv)"
        )

        if not file_path:
            return

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

    def browse_logo(self):
        """Select channel logo."""

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Logo",
            "",
            "Images (*.png *.jpg *.jpeg)"
        )

        if not file_path:
            return

        self.logo_card.set_path(file_path)

    def browse_output_folder(self):
        """Select output folder."""

        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Output Folder"
        )

        if not folder:
            return

        self.output_card.set_path(folder)

    def generate_project(self):
        if not self.video_card.path:
            QMessageBox.warning(
                self,
                "Missing Video",
                "Please choose a video."
            )
            return

        if not self.output_card.path:
            QMessageBox.warning(
                self,
                "Missing Output Folder",
                "Please choose an output folder."
            )
            return

        # -------------------------
        # Progress Dialog
        # -------------------------
        self.progress_dialog = ProgressDialog(self)
        self.progress_dialog.progress.setValue(0)
        self.progress_dialog.status.setText(
            "Preparing..."
        )
        self.progress_dialog.show()

        # -------------------------
        # Worker Thread
        # -------------------------
        self.thread = QThread()
        self.worker = ClipPipelineWorker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(
            lambda: self.worker.run(
                self.video_card.path,
                self.output_card.path
            )
        )

        self.worker.progress.connect(self.update_progress)
        self.worker.finished.connect(self.pipeline_finished)
        self.worker.error.connect(self.pipeline_failed)

        self.thread.start()
        
    def update_progress(self, value, message):
        self.progress_dialog.progress.setValue(value)
        self.progress_dialog.status.setText(message)
    
    def pipeline_finished(self, clips):
        self.thread.quit()
        self.thread.wait()

        self.progress_dialog.close()

        self.generationFinished.emit()

        message = QMessageBox(self)

        message.setWindowTitle("Generation Complete")

        message.setIcon(QMessageBox.Information)

        message.setText(
            f"Successfully generated {len(clips)} clip(s)."
        )

        open_button = message.addButton(
            "📂 Open Output Folder",
            QMessageBox.ActionRole
        )

        message.addButton(
            QMessageBox.Ok
        )

        message.exec()

        if message.clickedButton() == open_button:
            QDesktopServices.openUrl(
                QUrl.fromLocalFile(
                    self.output_card.path
                )
            )

    def pipeline_failed(self, message):
        from PySide6.QtWidgets import QMessageBox
        self.thread.quit()
        self.thread.wait()
        self.progress_dialog.close()
        QMessageBox.critical(
            self,
            "Pipeline Error",
            message
        )
