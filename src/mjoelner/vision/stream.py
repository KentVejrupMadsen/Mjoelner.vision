from mjoelner.vision \
    import VisionApi

from mjoelner.vision.hooks \
    import StreamOnHook

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

        self.events: list | None = None
        self.hooks: list | None = None

        self.setup()

    def __del__(
        self
    ):
        self.release()

        del                         \
            self.capture_device,    \
            self.is_done,           \
            self.buffer_image,      \
            self.events,            \
            self.hooks

    def setup(self):
        self.get_hooks().append(
            StreamOnHook(
                self
            )
        )

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

        self.update_hooks()
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

    def update_hooks(
        self
    ):
        for hook in self.get_hooks():
            hook.run()

    def get_hooks(
        self
    ) -> list:
        if self.is_hooks_none():
            self.set_hooks(
                list()
            )

        return self.hooks

    def set_hooks(
        self,
        value: list
    ) -> None:
        self.hooks = value

    def is_hooks_none(
        self
    ) -> bool:
        return self.hooks is None

    def is_hooks_empty(
        self
    ):
        return bool(
            len(
                self.get_hooks()
            )
            ==
            zero()
        )

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
            len(
                self.events
            )
            ==
            zero()
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
