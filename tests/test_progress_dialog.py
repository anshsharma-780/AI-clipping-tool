import sys
import os

from PySide6.QtWidgets import QApplication

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui.progress_dialog import ProgressDialog


app = QApplication(sys.argv)

dialog = ProgressDialog()

dialog.progress.setValue(40)

dialog.status.setText(
    "Detecting Highlights..."
)

dialog.show()

app.exec()