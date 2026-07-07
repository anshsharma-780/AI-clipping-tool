from core.project_manager import ProjectManager

manager = ProjectManager()

project = {

    "video":
        "input/video.mp4",

    "logo":
        "assets/logo.png",

    "output":
        "output/",

    "subtitle_theme":
        "instagram",

    "smart_crop":
        True

}

manager.save_project(
    "demo.aiclip",
    project
)

loaded = manager.load_project(
    "demo.aiclip"
)

print(loaded)