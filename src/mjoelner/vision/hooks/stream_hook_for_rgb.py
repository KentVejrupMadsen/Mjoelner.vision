from mjoelner.vision.hooks \
    import StreamConversionHook


class StreamHookForRGB(
    StreamConversionHook
):
    def __init__(
        self,
        vision,
        vsp
    ):
        super().__init__(
            vision
        )
        self.properties = vsp

    def get_properties(
        self
    ):
        return self.properties

    def set_properties(
        self,
        properties
    ) -> None:
        self.properties = properties

    def on_condition(
        self
    ) -> bool:
        return self.get_properties()        \
                   .get_convert_to_rgb()

    def run_hook(
        self
    ) -> None:
        image = self.get_vision_interface().get_buffer_image()
        image = self.get_conversion().convert(
            image
        )

        self.get_vision_interface().set_buffer_image(
            image
        )

