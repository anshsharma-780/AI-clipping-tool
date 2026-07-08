from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QCheckBox,
)

from config.app_settings import settings


class SettingsDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Settings")
        self.resize(450, 420)

        layout = QVBoxLayout(self)

        # ------------------------
        # Caption Style
        # ------------------------

        row = QHBoxLayout()

        row.addWidget(QLabel("Caption Style"))

        self.theme = QComboBox()

        self.theme.addItems([
            "TikTok",
            "Instagram",
            "Minimal"
        ])

        current_theme = settings.get("subtitle_theme")

        if current_theme == "tiktok":
            self.theme.setCurrentText("TikTok")
        elif current_theme == "instagram":
            self.theme.setCurrentText("Instagram")
        else:
            self.theme.setCurrentText("Minimal")

        row.addWidget(self.theme)

        layout.addLayout(row)

        # ------------------------
        # Export Quality
        # ------------------------

        row = QHBoxLayout()

        row.addWidget(QLabel("Export Quality"))

        self.export_quality = QComboBox()

        self.export_quality.addItems([
            "High",
            "Medium",
            "Fast"
        ])

        current_crf = settings.get("crf")

        if current_crf <= 18:
            self.export_quality.setCurrentText("High")
        elif current_crf <= 22:
            self.export_quality.setCurrentText("Medium")
        else:
            self.export_quality.setCurrentText("Fast")

        row.addWidget(self.export_quality)

        layout.addLayout(row)

        # ------------------------
        # Logo Size
        # ------------------------

        row = QHBoxLayout()

        row.addWidget(QLabel("Logo Size"))

        self.logo_size = QComboBox()

        self.logo_size.addItems([
            "Small",
            "Medium",
            "Large"
        ])
        current_logo = settings.get("logo_scale")

        # Map numeric scale values to combo box text
        if current_logo == 0.08:
            current_logo = "Small"
        elif current_logo == 0.16:
            current_logo = "Large"
        else:
            # default to Medium for 0.12, None, or any other value
            current_logo = "Medium"

        self.logo_size.setCurrentText(current_logo)

        row.addWidget(self.logo_size)

        layout.addLayout(row)

        # ------------------------
        # AI Smart Crop
        # ------------------------

        self.smart_crop = QCheckBox(
            "Enable AI Smart Crop"
        )

        self.smart_crop.setChecked(
            settings.get("smart_crop")
        )

        layout.addWidget(self.smart_crop)

        layout.addStretch()

        # ------------------------
        # Save Button
        # ------------------------

        save = QPushButton("Save Settings")

        save.clicked.connect(self.save_settings)

        layout.addWidget(save)

    def save_settings(self):

        # Caption Style

        settings.set(
            "subtitle_theme",
            self.theme.currentText().lower()
        )

        # Export Quality

        quality = self.export_quality.currentText()

        if quality == "High":
            settings.set("crf", 18)

        elif quality == "Medium":
            settings.set("crf", 22)

        else:
            settings.set("crf", 26)

        # Logo Size

        settings.set(
            "logo_scale",
            self.logo_size.currentText().lower()
        )

        # Smart Crop

        settings.set(
            "smart_crop",
            self.smart_crop.isChecked()
        )

        settings.save()

        self.accept()