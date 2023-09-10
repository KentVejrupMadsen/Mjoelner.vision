from os.path \
    import isfile

from mjoelner.vision.stream \
    import VisionStream


class VideoToFrames:
    def __init__(
        self,
        path_to_file: str
    ):
        if not isfile(
            path_to_file
        ):
            raise IOError(
                'File not found.'
            )

        self.stream = VisionStream(
            path_to_file
        )

    def __del__(self):
        del self.stream
    