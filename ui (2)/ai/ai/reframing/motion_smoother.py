class MotionSmoother:
    """
    Smooth crop movement using exponential smoothing.
    """

    def __init__(self, alpha=0.25):
        self.alpha = alpha

    def smooth(self, values):

        if not values:
            return []

        smoothed = [values[0]]

        current = values[0]

        for value in values[1:]:

            current = (
                self.alpha * value +
                (1 - self.alpha) * current
            )

            smoothed.append(int(current))

        return smoothed