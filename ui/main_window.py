from ui.transcript_viewer import TranscriptViewer
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QFrame,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QSizePolicy,
    QStatusBar,
)

from ui.project_setup_widget import ProjectSetupWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Clipping Tool")
        self.resize(1400, 850)
        self.setMinimumSize(1200, 700)

        self.build_ui()

    def build_ui(self):

        # ==========================
        # Central Widget
        # ==========================

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        root_layout = QHBoxLayout(central_widget)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        # ==========================
        # Sidebar
        # ==========================

        sidebar = QFrame()
        sidebar.setFixedWidth(220)

        sidebar.setStyleSheet("""
            QFrame{
                background:#1f1f1f;
            }

            QPushButton{
                background:transparent;
                color:white;
                border:none;
                text-align:left;
                padding:12px;
                font-size:14px;
            }

            QPushButton:hover{
                background:#2d2d2d;
            }
        """)

        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(15,20,15,20)
        sidebar_layout.setSpacing(10)

        logo = QLabel("AI Clipping Tool")

        logo.setStyleSheet("""
            color:white;
            font-size:22px;
            font-weight:bold;
        """)

        sidebar_layout.addWidget(logo)
        sidebar_layout.addSpacing(25)

        self.home_button = QPushButton("🏠  Home")
        self.projects_button = QPushButton("📁  Projects")
        self.settings_button = QPushButton("⚙  Settings")

        sidebar_layout.addWidget(self.home_button)
        sidebar_layout.addWidget(self.projects_button)
        sidebar_layout.addWidget(self.settings_button)

        sidebar_layout.addStretch()

        version = QLabel("Version 0.2.3.1")

        version.setStyleSheet("""
            color:#888888;
            font-size:11px;
        """)

        sidebar_layout.addWidget(version)

        # ==========================
        # Right Panel
        # ==========================

        right_panel = QWidget()

        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(0,0,0,0)
        right_layout.setSpacing(0)

        # ==========================
        # Header
        # ==========================

        header = QFrame()

        header.setFixedHeight(65)

        header.setStyleSheet("""
            QFrame{
                background:#2b2b2b;
                border-bottom:1px solid #3a3a3a;
            }
        """)

        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(20,10,20,10)

        title = QLabel("🚀 AI Clipping Tool")

        title.setStyleSheet("""
            color:white;
            font-size:24px;
            font-weight:bold;
        """)

        subtitle = QLabel("Professional AI Video Clipping")

        subtitle.setStyleSheet("""
            color:#aaaaaa;
            font-size:12px;
        """)

        title_layout = QVBoxLayout()
        title_layout.setSpacing(2)
        title_layout.addWidget(title)
        title_layout.addWidget(subtitle)

        header_layout.addLayout(title_layout)
        header_layout.addStretch()

        self.status_indicator = QLabel("● Ready")

        self.status_indicator.setStyleSheet("""
            color:#43d854;
            font-size:13px;
            font-weight:bold;
        """)

        header_layout.addWidget(self.status_indicator)
        # ==========================
        # Project Setup Widget
        # ==========================

        self.project_setup_widget = ProjectSetupWidget()
        self.project_setup_widget.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.addWidget(self.project_setup_widget)

        content_widget = QWidget()
        content_widget.setLayout(content_layout)

        # Add widgets to right panel
        right_layout.addWidget(header)
        right_layout.addWidget(content_widget)

        # Add sidebar and right panel
        root_layout.addWidget(sidebar)
        root_layout.addWidget(right_panel)

        # ==========================
        # Status Bar
        # ==========================

        status_bar = QStatusBar()
        status_bar.showMessage("Ready")
        self.setStatusBar(status_bar)

        self.status_bar = status_bar