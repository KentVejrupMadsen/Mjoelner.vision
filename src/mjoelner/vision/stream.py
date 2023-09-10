from mjoelner.vision \
    import VisionConversion

from cv2 \
    import VideoCapture


class VisionStream:
    def __init__(
        self,
        device_capture: str
    ):
        self.capture_device = VideoCapture(
            device_capture
        )
        self.conversion = VisionConversion()
        self.is_done: bool = False

    def __del__(
        self
    ):
        self.release()
        del                         \
            self.capture_device,    \
            self.conversion,        \
            self.is_done

    def is_open(
        self
    ):
        return self.get_capture_device() \
                   .isOpened()

    def flag_is_done(
        self
    ):
        self.set_is_done(
            True
        )

    def get_is_done(
        self
    ) -> bool:
        return self.is_done

    def set_is_done(
        self,
        value: bool
    ) -> None:
        self.is_done = value

    def stream(
        self
    ) -> list:
        frame = self.capture()

        if frame is None:
            raise IOError('Stream is done')

        return frame

    def capture(
        self
    ):
        cd = self.get_capture_device()

        returnable, image = cd.read()

        if not returnable:
            self.flag_is_done()
            return None

        image = self.conversion.convert(
            image
        )
        return image

    def release(
        self
    ):
        self.get_capture_device() \
            .release()

    def get_capture_device(
        self
    ) -> VideoCapture:
        return self.capture_device

    def set_capture_device(
        self,
        value: VideoCapture
    ) -> None:
        self.capture_device = value
