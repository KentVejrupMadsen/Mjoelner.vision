from mjoelner.vision.hooks.visionhook \
    import VisionHook


class StreamOnHook(
    VisionHook
):
    def __init__(self):
        super().__init__()
        self.value: bool = True

    def on_condition(
        self
    ) -> bool:
        return self.get_value()

    def get_value(
        self
    ) -> bool:
        return self.value

    def set_value(
        self,
        value: bool
    ) -> None:
        self.value = value
