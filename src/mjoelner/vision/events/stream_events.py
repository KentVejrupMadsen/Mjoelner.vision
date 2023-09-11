from abc \
    import ABC, abstractmethod

from mjoelner.vision \
    import VisionStream


class StreamEvent(
    ABC
):
    def __init__(
        self,
        stream: VisionStream
    ):
        self.stream = stream

    def update(
        self
    ) -> None:
        if self.precondition():
            self.run()

    @abstractmethod
    def run(
        self
    ) -> None:
        raise NotImplemented(
            'Method not implemented'
        )

    @abstractmethod
    def precondition(
        self
    ) -> bool:
        raise NotImplemented(
            'Method not implemented'
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
