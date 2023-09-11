from mjoelner.vision.hooks.visionhook \
    import VisionHook


class StreamHookForRGB(
    VisionHook
):
    def __init__(
        self,
        vsp
    ):
        super().__init__()
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
