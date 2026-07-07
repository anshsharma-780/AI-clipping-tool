import sys

from PySide6.QtWidgets import QApplication

from ui.video_player_widget import VideoPlayerWidget

app = QApplication(sys.argv)

player = VideoPlayerWidget()

video = input("Video:\n")

player.load_video(video)

player.resize(900, 650)

player.show()

app.exec()