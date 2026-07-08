from pathlib import Path
from datetime import datetime


class Logger:

    def __init__(self):

        self.log_dir = Path("logs")

        self.log_dir.mkdir(exist_ok=True)

        self.log_file = self.log_dir / "application.log"

    def log(self, level, message):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        line = f"[{timestamp}] [{level}] {message}\n"

        with open(self.log_file, "a", encoding="utf-8") as f:

            f.write(line)

        print(line, end="")

    def info(self, message):

        self.log("INFO", message)

    def warning(self, message):

        self.log("WARNING", message)

    def error(self, message):

        self.log("ERROR", message)


logger = Logger()