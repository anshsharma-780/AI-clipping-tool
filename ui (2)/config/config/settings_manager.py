import json
from pathlib import Path

from config.defaults import DEFAULT_SETTINGS


SETTINGS_FILE = Path("settings.json")


class SettingsManager:

    def load(self):

        if not SETTINGS_FILE.exists():

            return DEFAULT_SETTINGS.copy()

        try:

            with open(
                SETTINGS_FILE,
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)

        except Exception:

            return DEFAULT_SETTINGS.copy()

        settings = DEFAULT_SETTINGS.copy()

        settings.update(data)

        return settings

    def save(self, settings):

        with open(
            SETTINGS_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                settings,
                f,
                indent=4
            )