from mjoelner.vision.hooks \
    import StreamConversionHook


class StreamOnHook(
    StreamConversionHook
):
    def __init__(
        self,
        vision
    ):
        super().__init__(
            vision
        )

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

    def run_hook(
        self
    ) -> None:
        image = self.get_vision_interface().get_buffer_image()

        image = self.conversion.convert(
            image
        )

        self.get_vision_interface().set_buffer_image(
            image
        )

