from mjoelner.vision        \
    import                  \
    Hook,                   \
    VisionStreamProperties


class StreamHookForRGB(
    Hook
):
    def __init__(
        self,
        vsp: VisionStreamProperties
    ):
        super().__init__()
        self.properties = vsp

    def get_properties(
        self
    ) -> VisionStreamProperties:
        return self.properties

    def set_properties(
        self,
        properties: VisionStreamProperties
    ) -> None:
        self.properties = properties

    def on_condition(
        self
    ) -> bool:
        return self.get_properties()        \
                   .get_convert_to_rgb()
