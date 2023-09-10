from mjoelner.vision.conversion \
    import VisionConversion

from cv2 \
    import VideoCapture


class VisionStream:
    def __init__(
        self,
        device_capture: str
    ):
        self.capture = VideoCapture(
            device_capture
        )

    def __del__(self):
        self.capture.release()

    