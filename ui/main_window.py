from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
) 

from core.app_info import (
    APP_NAME,
    VERSION,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"{APP_NAME} v{VERSION}")
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.build_ui()

    def build_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        root = QHBoxLayout()
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ==========================
        # Sidebar
        # ==========================

        sidebar = QFrame()
        sidebar.setFixedWidth(220)

        sidebar.setStyleSheet("""
            background:#202020;
        """)

        side_layout = QVBoxLayout()

        logo = QLabel("AI Clipping Tool")
        logo.setFont(QFont("Segoe UI", 14, QFont.Bold))
        logo.setStyleSheet("color:white; padding:20px;")

        side_layout.addWidget(logo)

        for text in [
            "🏠 Home",
            "📁 Projects",
            "⚙ Settings"
        ]:

            btn = QPushButton(text)

            btn.setCursor(Qt.PointingHandCursor)

            btn.setMinimumHeight(42)

            btn.setStyleSheet("""
                QPushButton{
                    color:white;
                    background:#2d2d2d;
                    border:none;
                    text-align:left;
                    padding-left:15px;
                }

                QPushButton:hover{
                    background:#3a3a3a;
                }
            """)

            side_layout.addWidget(btn)

        side_layout.addStretch()

        sidebar.setLayout(side_layout)

        # ==========================
        # Right Side
        # ==========================

        right = QWidget()

        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(0,0,0,0)

        # Header

        header = QFrame()
        header.setFixedHeight(60)

        header.setStyleSheet("""
            background:#252526;
            color:white;
        """)

        header_layout = QHBoxLayout()

        title = QLabel(f"{APP_NAME}")

        title.setFont(QFont("Segoe UI", 13, QFont.Bold))

        header_layout.addWidget(title)

        header_layout.addStretch()

        version = QLabel(f"v{VERSION}")

        header_layout.addWidget(version)

        header.setLayout(header_layout)

        # ==========================
        # Workspace
        # ==========================

workspace = QFrame()

workspace.setStyleSheet("""
    background:#2b2b2b;
""")

workspace_layout = QVBoxLayout()

workspace_layout.setAlignment(Qt.AlignCenter)

# Card

card = QFrame()

card.setFixedWidth(700)

card.setStyleSheet("""
QFrame{
    background:#353535;
    border-radius:12px;
}
""")

card_layout = QVBoxLayout()

card_layout.setContentsMargins(30,30,30,30)

# Title

title = QLabel("Project Setup")

title.setAlignment(Qt.AlignCenter)

title.setStyleSheet("""
color:white;
font-size:24px;
font-weight:bold;
""")

card_layout.addWidget(title)

card_layout.addSpacing(20)

# ---------- INPUT VIDEO ----------

video_label = QLabel("🎥 Input Video")
video_label.setStyleSheet("color:white;")

card_layout.addWidget(video_label)

self.video_path = QLabel("No video selected")

self.video_path.setMinimumHeight(35)

self.video_path.setStyleSheet("""
background:#222;
color:#bbbbbb;
padding:8px;
border-radius:6px;
""")

card_layout.addWidget(self.video_path)

card_layout.addSpacing(15)

# ---------- LOGO ----------

logo_label = QLabel("🖼 Logo")

logo_label.setStyleSheet("color:white;")

card_layout.addWidget(logo_label)

self.logo_path = QLabel("No logo selected")

self.logo_path.setMinimumHeight(35)

self.logo_path.setStyleSheet("""
background:#222;
color:#bbbbbb;
padding:8px;
border-radius:6px;
""")

card_layout.addWidget(self.logo_path)

card_layout.addSpacing(15)

# ---------- OUTPUT ----------

output_label = QLabel("📂 Output Folder")

output_label.setStyleSheet("color:white;")

card_layout.addWidget(output_label)

self.output_path = QLabel("No output folder selected")

self.output_path.setMinimumHeight(35)

self.output_path.setStyleSheet("""
background:#222;
color:#bbbbbb;
padding:8px;
border-radius:6px;
""")

card_layout.addWidget(self.output_path)

card_layout.addSpacing(25)

# ---------- VIDEO INFO ----------

info = QLabel("Video Information")

info.setStyleSheet("""
color:white;
font-size:18px;
font-weight:bold;
""")

card_layout.addWidget(info)

card_layout.addSpacing(10)

for text in [
    "Duration : --",
    "Resolution : --",
    "FPS : --"
]:
    lbl = QLabel(text)
    lbl.setStyleSheet("color:#cccccc;")
    card_layout.addWidget(lbl)

card_layout.addSpacing(30)

continue_button = QPushButton("Continue")

continue_button.setMinimumHeight(45)

continue_button.setStyleSheet("""
QPushButton{
    background:#0078D4;
    color:white;
    border:none;
    border-radius:8px;
    font-size:15px;
}

QPushButton:hover{
    background:#2196F3;
}
""")

card_layout.addWidget(continue_button)

card.setLayout(card_layout)

workspace_layout.addWidget(card)

workspace.setLayout(workspace_layout)

        # Status bar

status = QFrame()

status.setFixedHeight(32)

status.setStyleSheet("""
            background:#202020;
            color:#cccccc;
        """)

status_layout = QHBoxLayout()

self.status_label = QLabel("Ready")

status_layout.addWidget(self.status_label)

status_layout.addStretch()

status.setLayout(status_layout)

right_layout.addWidget(header)

right_layout.addWidget(workspace)

right_layout.addWidget(status)

right.setLayout(right_layout)

root.addWidget(sidebar)
root.addWidget(right)

central.setLayout(root)