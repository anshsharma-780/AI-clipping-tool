class CropCalculator:
    """
    Calculates the optimal 9:16 crop around a detected face.
    """

    def __init__(self):

        self.target_ratio = 9 / 16

    def calculate(
        self,
        frame_width,
        frame_height,
        face
    ):

        x, y, w, h = face

        # Face center
        center_x = x + w / 2
        center_y = y + h / 2

        # Crop width for a 9:16 frame
        crop_width = int(frame_height * self.target_ratio)
        crop_height = frame_height

        crop_x = int(center_x - crop_width / 2)
        crop_y = 0

        # Clamp inside frame
        crop_x = max(0, crop_x)

        if crop_x + crop_width > frame_width:
            crop_x = frame_width - crop_width

        return {
            "x": crop_x,
            "y": crop_y,
            "width": crop_width,
            "height": crop_height,
        }