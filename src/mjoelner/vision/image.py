from mjoelner.vision \
    import VisionApi

from mjoelner.vision.conversions \
    import VisionConversion

from cv2 \
    import imread


class VisionImage(
    VisionApi
):
    def __init__(self):
        super().__init__()

    def __del__(self):
        pass
