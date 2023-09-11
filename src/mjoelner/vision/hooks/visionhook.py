from abc            \
    import          \
    ABC,            \
    abstractmethod

from mjoelner.vision \
    import VisionApi


class VisionHook(
    ABC
):
    def __init__(
        self,
        vision: VisionApi
    ):
        super().__init__()
        self.vision = vision

    def set_vision_interface(
        self,
        value: VisionApi
    ) -> None:
        self.vision = value

    def get_vision_interface(
        self
    ) -> VisionApi:
        return self.vision

    @abstractmethod
    def on_condition(self) -> bool:
        raise NotImplemented(
            'not implemented method used.'
        )

    @abstractmethod
    def run_hook(self) -> None:
        raise NotImplemented(
            'method not implemented'
        )

    def run(self) -> None:
        if self.on_condition():
            self.run_hook()
