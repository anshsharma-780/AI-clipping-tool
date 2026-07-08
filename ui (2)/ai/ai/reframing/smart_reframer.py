import cv2

from ai.reframing.face_detector import FaceDetector
from ai.reframing.crop_calculator import CropCalculator


class SmartReframer:

    def __init__(self):

        self.detector = FaceDetector()

        self.calculator = CropCalculator()

    def analyze(
        self,
        video_path,
        sample_every=30
    ):

        cap = cv2.VideoCapture(video_path)

        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        frame_index = 0

        crops = []

        while True:

            success, frame = cap.read()

            if not success:
                break

            if frame_index % sample_every == 0:

                faces = self.detector.detect(frame)

                if len(faces):

                    crop = self.calculator.calculate(
                        frame_width,
                        frame_height,
                        faces[0]
                    )

                    crops.append(crop)

            frame_index += 1

        cap.release()

        if not crops:

            return None

        avg_x = int(sum(c["x"] for c in crops) / len(crops))

        return {

            "x": avg_x,

            "y": 0,

            "width": crops[0]["width"],

            "height": crops[0]["height"]

        }