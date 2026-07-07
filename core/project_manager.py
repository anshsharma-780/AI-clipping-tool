import json
from pathlib import Path


class ProjectManager:

    def save_project(self, filename, data):

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load_project(self, filename):

        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)