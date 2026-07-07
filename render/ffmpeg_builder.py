from pathlib import Path

from config.app_settings import settings
from render.render_job import RenderJob
from render.export_manager import ExportManager


class FFmpegBuilder:

    def build(self, job: RenderJob):

        Path(job.output_video).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        # -----------------------------
        # Export Profile
        # -----------------------------

        manager = ExportManager()
        profile = manager.get_profile()

        command = [
            "ffmpeg",
            "-y",
            "-ss", str(job.clip_start),
            "-to", str(job.clip_end),
            "-i", job.input_video,
        ]

        filter_chain = []

        current = "[0:v]"

        # -----------------------------
        # Crop
        # -----------------------------

        if job.crop:

            crop = job.crop

            filter_chain.append(

                f"{current}"
                f"crop={crop['width']}:{crop['height']}:{crop['x']}:{crop['y']}"
                f"[crop]"

            )

            current = "[crop]"

        # -----------------------------
        # ASS Subtitles
        # -----------------------------

        if job.subtitles:

            subtitle = (
                job.subtitles
                .replace("\\", "/")
                .replace(":", "\\:")
            )

            filter_chain.append(

                f"{current}"
                f"ass='{subtitle}'"
                f"[subtitle]"

            )

            current = "[subtitle]"

        # -----------------------------
        # Logo
        # -----------------------------

        if job.logo:

            logo_path = str(
                Path(
                    job.logo.strip().strip('"')
                )
            )

            command.extend([
                "-i",
                logo_path
            ])

            positions = {

                "top-right":
                    "main_w-overlay_w-30:30",

                "top-left":
                    "30:30",

                "bottom-right":
                    "main_w-overlay_w-30:main_h-overlay_h-30",

                "bottom-left":
                    "30:main_h-overlay_h-30",

            }

            overlay = positions.get(
                job.logo_position,
                positions["top-right"]
            )

            # -----------------------------
            # Logo Size
            # -----------------------------

            logo_scale = settings.get("logo_scale")

            if logo_scale == "small":
                scale = "0.08"

            elif logo_scale == "large":
                scale = "0.16"

            else:
                scale = "0.12"

            filter_chain.append(

                f"[1:v]scale=iw*{scale}:-1[logo]"

            )

            filter_chain.append(

                f"{current}"
                f"[logo]"
                f"overlay={overlay}"
                "[final]"

            )

            current = "[final]"

        # -----------------------------
        # Filter Graph
        # -----------------------------

        if filter_chain:

            command.extend([
                "-filter_complex",
                ";".join(filter_chain)
            ])

            command.extend([
                "-map",
                current
            ])

        command.extend([
            "-map",
            "0:a?"
        ])

        # -----------------------------
        # Video Export
        # -----------------------------

        command.extend([
            "-c:v",
            "libx264",

            "-preset",
            profile.preset,

            "-crf",
            str(profile.crf),

            "-c:a",
            "copy",

            job.output_video
        ])

        return command