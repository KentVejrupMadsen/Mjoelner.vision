from abc        \
    import      \
    ABC,        \
    abstractmethod

from mjoelner.vision \
    import VisionStream


class VisionAdapter(
    ABC
):
    def __init__(
        self,
        stream: VisionStream
    ):
        super().__init__()
        self.stream: VisionStream = stream

    @abstractmethod
    def retrieve_image_as(
        self
    ):
        raise NotImplemented(
            'Method not implemented.'
        )

    def get_stream(
        self
    ) -> VisionStream:
        return self.stream

    def set_stream(
        self,
        value: VisionStream
    ) -> None:
        self.stream = value

