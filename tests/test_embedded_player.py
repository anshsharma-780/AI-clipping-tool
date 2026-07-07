import sys

from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout(window)

video = QVideoWidget()
layout.addWidget(video)

player = QMediaPlayer()
audio = QAudioOutput()

player.setAudioOutput(audio)
player.setVideoOutput(video)

path = input("Video:\n")

player.setSource(QUrl.fromLocalFile(path))

player.play()

window.resize(900, 600)
window.show()

app.exec()