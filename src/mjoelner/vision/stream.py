from mjoelner.vision    \
    import              \
    VisionConversion,   \
    Hook

from mjoelner.vision.setup.setup_conversion \
    import setup_conversion

from cv2 \
    import VideoCapture

from numpy \
    import ndarray


class VisionStream:
    def __init__(
        self,
        device_capture: str,
        automatic_conversion: bool = True,
        conversion_type: str = 'on'
    ):
        self.capture_device = VideoCapture(
            device_capture
        )

        self.hook: Hook | None = None
        self.is_done: bool = False

        self.conversion: VisionConversion | None = VisionConversion()

        if automatic_conversion:
            setup_conversion(
                self,
                conversion_type
            )

    def __del__(
        self
    ):
        self.release()

        del                         \
            self.capture_device,    \
            self.conversion,        \
            self.is_done,           \
            self.hook

    # On action
    def stream(
        self
    ) -> ndarray:
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

        if self.is_hook_instantiated():
            if self.get_hook().on_condition():
                image = self.conversion.convert(
                    image
                )

        return image

    # State Management
    def is_hook_empty(
        self
    ) -> bool:
        return self.hook is None

    def is_hook_instantiated(
        self
    ) -> bool:
        return not self.is_hook_empty()

    def get_hook(
        self
    ) -> Hook | None:
        return self.hook

    def set_hook(
        self,
        value: Hook
    ) -> None:
        self.hook = value

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
