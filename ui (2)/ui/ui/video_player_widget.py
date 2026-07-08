from pathlib import Path

from PySide6.QtCore import Qt, QUrl
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QSlider,
)

from PySide6.QtMultimedia import (
    QMediaPlayer,
    QAudioOutput,
)

from PySide6.QtMultimediaWidgets import QVideoWidget


class VideoPlayerWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.player = QMediaPlayer(self)
        self.audio = QAudioOutput(self)

        self.player.setAudioOutput(self.audio)

        self.audio.setVolume(1.0)

        layout = QVBoxLayout(self)

        # ==========================
        # Video Area
        # ==========================

        self.video = QVideoWidget()

        self.video.setMinimumSize(800, 450)

        self.player.setVideoOutput(self.video)

        layout.addWidget(self.video)

        # ==========================
        # Controls
        # ==========================

        controls = QHBoxLayout()

        self.play_btn = QPushButton("▶")
        self.pause_btn = QPushButton("⏸")
        self.stop_btn = QPushButton("⏹")

        controls.addWidget(self.play_btn)
        controls.addWidget(self.pause_btn)
        controls.addWidget(self.stop_btn)

        controls.addStretch()

        self.time_label = QLabel("00:00 / 00:00")

        controls.addWidget(self.time_label)

        layout.addLayout(controls)

        # ==========================
        # Timeline
        # ==========================

        self.slider = QSlider(Qt.Horizontal)

        self.slider.setRange(0, 0)

        layout.addWidget(self.slider)

        # ==========================
        # Signals
        # ==========================

        self.play_btn.clicked.connect(self.player.play)

        self.pause_btn.clicked.connect(self.player.pause)

        self.stop_btn.clicked.connect(self.player.stop)

        self.slider.sliderMoved.connect(self.player.setPosition)

        self.player.positionChanged.connect(self.position_changed)

        self.player.durationChanged.connect(self.duration_changed)

        self.player.errorOccurred.connect(self.player_error)

        self.player.mediaStatusChanged.connect(self.media_status)
        self.player.playbackStateChanged.connect(self.playback_state)

    # =====================================================

    def load_video(self, path):

        absolute_path = str(Path(path).resolve())

        print("\n==============================")
        print("Loading Video")
        print(absolute_path)
        print("==============================")

        self.player.stop()

        url = QUrl.fromLocalFile(absolute_path)

        self.player.setSource(url)

        

    # =====================================================

    def duration_changed(self, duration):

        self.slider.setRange(0, duration)

    # =====================================================

    def position_changed(self, position):

        self.slider.blockSignals(True)

        self.slider.setValue(position)

        self.slider.blockSignals(False)

        duration = self.player.duration()

        self.time_label.setText(

            f"{self.format_time(position)} / "
            f"{self.format_time(duration)}"

        )

    # =====================================================

    def format_time(self, ms):

        seconds = ms // 1000

        minutes = seconds // 60

        seconds = seconds % 60

        return f"{minutes:02}:{seconds:02}"

    # =====================================================

    def player_error(self, error, error_string):

        print("\nPLAYER ERROR")
        print(error)
        print(error_string)

    # =====================================================

    def media_status(self, status):

        print("Media Status:", status)

        if status == QMediaPlayer.MediaStatus.LoadedMedia:
            print("Media loaded. Starting playback...")
            self.player.play()
    def playback_state(self, state):

            print("Playback State:", state)