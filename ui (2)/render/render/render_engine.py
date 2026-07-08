import subprocess

from render.ffmpeg_builder import FFmpegBuilder


class RenderEngine:

    def __init__(self):

        self.builder = FFmpegBuilder()

    def render(self, job):

        command = self.builder.build(job)

        result = subprocess.run(

            command,

            capture_output=True,

            text=True

        )

        if result.returncode != 0:

            raise RuntimeError(result.stderr)

        return job.output_video