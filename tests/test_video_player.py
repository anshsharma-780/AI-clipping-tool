import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

from PySide6.QtWidgets import QWidget, QVBoxLayout


app = QApplication(sys.argv)

window = QWidget()

layout = QVBoxLayout(window)

video = QVideoWidget()

layout.addWidget(video)

player = QMediaPlayer()
audio = QAudioOutput()

player.setAudioOutput(audio)
player.setVideoOutput(video)

window.resize(900, 600)
window.show()

print("=" * 50)
print("Qt Multimedia Loaded Successfully")
print("=" * 50)

app.exec()