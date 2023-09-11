from abc \
    import ABC, abstractmethod

from numpy \
    import ndarray


class VisionApi(
    ABC
):
    def __init__(self):
        super().__init__()
        self.buffer_image: ndarray | None = None

    def get_buffer_image(
        self
    ) -> ndarray:
        return self.buffer_image

    def set_buffer_image(
        self,
        image: ndarray
    ) -> None:
        self.buffer_image = image

    def is_buffer_image_empty(
        self
    ) -> bool:
        return self.buffer_image is None
