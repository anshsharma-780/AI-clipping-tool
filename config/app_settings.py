from config.settings_manager import SettingsManager


class AppSettings:

    def __init__(self):

        self.manager = SettingsManager()

        self._settings = self.manager.load()

    def get(self, key, default=None):

        return self._settings.get(key, default)

    def set(self, key, value):

        self._settings[key] = value

    def save(self):

        self.manager.save(self._settings)

    def reload(self):

        self._settings = self.manager.load()

    def all(self):

        return self._settings.copy()


settings = AppSettings()