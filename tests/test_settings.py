from config.app_settings import settings

print("=" * 60)
print("CURRENT SETTINGS")
print("=" * 60)

print()

print("Subtitle Theme:")

print(settings.get("subtitle_theme"))

print()

print("Changing theme to Instagram...")

settings.set(
    "subtitle_theme",
    "instagram"
)

settings.save()

print()

print("Saved!")

print()

print("Reloading settings...")

settings.reload()

print()

print("Current Theme:")

print(settings.get("subtitle_theme"))