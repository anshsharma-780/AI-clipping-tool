from pathlib import Path

from processing.video.clip_generator import generate_clip


def test_generate_clip_uses_render_engine_for_overlays(tmp_path, monkeypatch):
    captured = {}

    class FakeRenderEngine:
        def render(self, job):
            captured["job"] = job
            return job.output_video

    monkeypatch.setattr(
        "processing.video.clip_generator.RenderEngine",
        lambda: FakeRenderEngine(),
    )

    output = generate_clip(
        input_video="input.mp4",
        output_folder=tmp_path,
        start_time=1.5,
        end_time=4.5,
        output_name="clip.mp4",
        subtitle_file="subtitles.ass",
        logo_path="logo.png",
    )

    assert output == str(tmp_path / "clip.mp4")
    job = captured["job"]
    assert job.input_video == "input.mp4"
    assert job.clip_start == 1.5
    assert job.clip_end == 4.5
    assert job.subtitles == "subtitles.ass"
    assert job.logo == "logo.png"
    assert job.logo_position == "top-right"
