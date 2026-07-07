import cv2
import mediapipe as mp


class FaceDetector:

    def __init__(self):

        self.face_detection = (
            mp.solutions.face_detection.FaceDetection(
                model_selection=1,
                min_detection_confidence=0.6
            )
        )

    def detect(self, image):

        rgb = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB
        )

        results = self.face_detection.process(rgb)

        faces = []

        if results.detections:

            h, w, _ = image.shape

            for detection in results.detections:

                bbox = detection.location_data.relative_bounding_box

                x = int(bbox.xmin * w)
                y = int(bbox.ymin * h)
                bw = int(bbox.width * w)
                bh = int(bbox.height * h)

                faces.append(
                    (
                        x,
                        y,
                        bw,
                        bh
                    )
                )

        return faces