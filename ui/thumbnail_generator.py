import subprocess
from pathlib import Path


class ThumbnailGenerator:

    def generate(
        self,
        video_path,
        output_image
    ):

        Path(output_image).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        command = [

            "ffmpeg",

            "-y",

            "-ss", "2",

            "-i", video_path,

            "-frames:v", "1",

            output_image

        ]

        subprocess.run(
            command,
            capture_output=True
        )

        return output_image