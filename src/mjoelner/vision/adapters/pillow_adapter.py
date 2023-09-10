from PIL.Image  \
    import      \
    Image,      \
    fromarray

from mjoelner.vision.adapters \
    import VisionAdapter


class VisionAdapterForPillow(
    VisionAdapter
):
    def __init__(
        self,
        stream
    ):
        super().__init__(
            stream
        )

    def retrieve_image_as(
        self
    ) -> Image:
        return fromarray(
            self.get_stream().get_buffer_image()
        )
