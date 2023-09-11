from mjoelner.vision.hooks.visionhook   \
    import                              \
    VisionHook,                         \
    abstractmethod

from mjoelner.vision.conversions        \
    import VisionConversion


class StreamConversionHook(
    VisionHook
):
    def __init__(
        self,
        vision
    ):
        super().__init__(
            vision
        )

        self.conversion: VisionConversion = VisionConversion()

    def get_conversion(
        self
    ):
        return self.conversion

    def set_conversion(
        self,
        value: VisionConversion
    ) -> None:
        self.conversion = value

    @abstractmethod
    def on_condition(
        self
    ) -> bool:
        raise NotImplemented('method not implemented')

    @abstractmethod
    def run_hook(
        self
    ) -> None:
        raise NotImplemented('method not implemented')

