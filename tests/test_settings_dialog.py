import sys

from PySide6.QtWidgets import QApplication

from ui.settings_dialog import SettingsDialog

app = QApplication(sys.argv)

dialog = SettingsDialog()

dialog.exec()