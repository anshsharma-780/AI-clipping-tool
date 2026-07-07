from core.pipeline_controller import PipelineController


pipeline = PipelineController()


pipeline.add_step(
    "Extract Audio",
    lambda: print("Extracting...")
)

pipeline.add_step(
    "Whisper",
    lambda: print("Transcribing...")
)

pipeline.add_step(
    "Highlight Detection",
    lambda: print("Finding highlights...")
)

pipeline.add_step(
    "Rendering",
    lambda: print("Rendering final clip...")
)

pipeline.run()