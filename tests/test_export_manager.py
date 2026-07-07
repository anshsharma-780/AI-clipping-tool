from render.export_manager import (
    ExportManager,
    HIGH,
    MEDIUM,
    FAST
)

manager = ExportManager()

print(manager.get_profile())

manager.set_profile(MEDIUM)

print(manager.get_profile())

manager.set_profile(FAST)

print(manager.get_profile())