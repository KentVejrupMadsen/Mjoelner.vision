from mjoelner.vision \
    import VisionApi

from mjoelner.vision.conversions \
    import VisionConversion

from mjoelner.vision.hooks \
    import VisionHook

from cv2 \
    import VideoCapture

from numpy \
    import ndarray


def zero() -> int:
    return 0


class VisionStream(
    VisionApi
):
    def __init__(
        self,
        device_capture: str
    ):
        super().__init__()
        self.capture_device = VideoCapture(
            device_capture
        )

        self.is_done: bool = False
        self.buffer_image: ndarray | None = None

        self.events: list | None = None

    def __del__(
        self
    ):
        self.release()
        del                         \
            self.capture_device,    \
            self.is_done,           \
            self.buffer_image,      \
            self.events

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

        self.set_buffer_image(
            image
        )

        self.update_events()
        return self.get_buffer_image()

    # State Management
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

    def get_keep_run(
        self
    ) -> bool:
        return not self.get_is_done()

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

    def get_events(
        self
    ) -> list:
        if self.is_events_none():
            self.set_events(
                list()
            )

        return self.events

    def set_events(
        self,
        value: list
    ) -> None:
        self.events = value

    def is_events_none(
        self
    ) -> bool:
        return self.events is None

    def is_events_empty(
        self
    ) -> bool:
        return bool(
            len(self.events) == zero()
        )

    def append_event(
        self,
        event
    ) -> None:
        self.get_events().append(
            event
        )

    def update_events(
        self
    ):
        for event in self.get_events():
            event.update()
