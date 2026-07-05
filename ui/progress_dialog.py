from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QVBoxLayout,
    QProgressBar,
    QPushButton,
)

from PySide6.QtCore import Qt


class ProgressDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setWindowTitle("AI Clipping Tool")
        self.setFixedSize(420, 220)

        layout = QVBoxLayout(self)

        self.title = QLabel("🚀 Generating AI Clips")
        self.title.setAlignment(Qt.AlignCenter)

        self.status = QLabel("Preparing...")
        self.status.setAlignment(Qt.AlignCenter)

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)

        self.cancel_button = QPushButton("Cancel")

        layout.addStretch()
        layout.addWidget(self.title)
        layout.addSpacing(10)
        layout.addWidget(self.status)
        layout.addWidget(self.progress)
        layout.addStretch()
        layout.addWidget(self.cancel_button)