import os
import cv2


def get_video_info(video_path):
    """
    Returns:
        duration (str)
        resolution (str)
        fps (str)
        file_size (str)
    """

    capture = cv2.VideoCapture(video_path)

    if not capture.isOpened():
        return None

    fps = capture.get(cv2.CAP_PROP_FPS)
    frame_count = capture.get(cv2.CAP_PROP_FRAME_COUNT)

    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    duration_seconds = frame_count / fps if fps else 0

    minutes = int(duration_seconds // 60)
    seconds = int(duration_seconds % 60)

    duration = f"{minutes:02}:{seconds:02}"

    resolution = f"{width} x {height}"

    file_size = os.path.getsize(video_path)

    file_size_mb = file_size / (1024 * 1024)

    capture.release()

    return {
        "duration": duration,
        "resolution": resolution,
        "fps": round(fps, 2),
        "size": f"{file_size_mb:.2f} MB"
    }