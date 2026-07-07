import sys

from PySide6.QtWidgets import QApplication

from ui.media_library import MediaLibrary

app = QApplication(sys.argv)

window = MediaLibrary()

window.resize(700,600)

window.show()

app.exec()