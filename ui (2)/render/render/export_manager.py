from dataclasses import dataclass

from config.app_settings import settings


@dataclass
class ExportProfile:

    name: str
    width: int
    height: int
    crf: int
    preset: str


HIGH = ExportProfile(
    "High",
    1080,
    1920,
    18,
    "slow"
)

MEDIUM = ExportProfile(
    "Medium",
    1080,
    1920,
    22,
    "medium"
)

FAST = ExportProfile(
    "Fast",
    1080,
    1920,
    26,
    "fast"
)


class ExportManager:

    def __init__(self):
        pass

    def get_profile(self):

        crf = settings.get("crf")

        if crf <= 18:
            return HIGH

        elif crf <= 22:
            return MEDIUM

        else:
            return FAST

    def set_profile(self, profile):

        settings.set("crf", profile.crf)
        settings.save()