from mjoelner.vision.conversions \
    import VisionConversion

from mjoelner.vision.setup \
    import setup_conversion

from mjoelner.vision.hooks \
    import Hook

from cv2 \
    import VideoCapture

from numpy \
    import ndarray


class VisionStream:
    def __init__(
        self,
        device_capture: str,
        automatic_conversion: bool = True,
        conversion_type: str = '2rgb'
    ):
        self.capture_device = VideoCapture(
            device_capture
        )

        self.hook: Hook | None = None
        self.is_done: bool = False

        self.conversion: VisionConversion | None = VisionConversion()
        self.buffer_image: ndarray | None = None

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
            self.hook,              \
            self.buffer_image

    # On action
    def stream(
        self
    ) -> ndarray:
        frame = self.capture()

        if frame is None:
            raise IOError(
                'Stream is done'
            )

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

        self.set_buffer_image(
            image
        )

        return self.get_buffer_image()

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

    def get_buffer_image(
        self
    ) -> ndarray:
        return self.buffer_image

    def set_buffer_image(
        self,
        image: ndarray
    ) -> None:
        self.buffer_image = image

    def is_buffer_image_empty(
        self
    ) -> bool:
        return self.buffer_image is None
