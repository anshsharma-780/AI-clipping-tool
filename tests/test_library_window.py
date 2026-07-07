import sys

from PySide6.QtWidgets import QApplication

from ui.library_window import LibraryWindow

app = QApplication(sys.argv)

window = LibraryWindow()

window.resize(1400,700)

window.show()

app.exec()