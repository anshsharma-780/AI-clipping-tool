from utils.logger import logger


class PipelineController:

    def __init__(self, progress_callback=None):

        self.steps = []
        self.progress_callback = progress_callback

    def add_step(self, name, callback):

        self.steps.append({
            "name": name,
            "callback": callback
        })

    def run(self):

        logger.info("Pipeline Started")

        total = len(self.steps)

        if total == 0:
            return

        for index, step in enumerate(self.steps):

            start = int((index / total) * 100)
            end = int(((index + 1) / total) * 100)

            if self.progress_callback:
                self.progress_callback(start, step["name"])

            logger.info(f"Running: {step['name']}")

            result = step["callback"]()

            logger.info(f"Completed: {step['name']}")

            if self.progress_callback:
                self.progress_callback(
                    end,
                    f"{step['name']} Complete"
                )

        logger.info("Pipeline Finished")