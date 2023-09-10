from cv2                    \
    import                  \
    CAP_PROP_FRAME_WIDTH,   \
    CAP_PROP_FRAME_HEIGHT,  \
    CAP_PROP_FPS,           \
    CAP_PROP_FRAME_COUNT,   \
    CAP_PROP_CONVERT_RGB,   \
    CAP_PROP_POS_FRAMES,    \
    CAP_PROP_POS_MSEC,      \
    CAP_PROP_BITRATE

from mjoelner.vision \
    import VisionStream


class VisionStreamProperties:
    def __init__(
        self,
        stream: VisionStream
    ):
        self.stream = stream

    def get_stream(
        self
    ) -> VisionStream:
        return self.stream

    def set_stream(
        self,
        value: VisionStream
    ) -> None:
        self.stream = value

    def get_frame_width(
        self
    ):
        return int(
            self._get_property(
                CAP_PROP_FRAME_WIDTH
            )
        )

    def get_frame_height(
        self
    ):
        return int(
            self._get_property(
                CAP_PROP_FRAME_HEIGHT
            )
        )

    def get_frames_per_second(
        self
    ):
        return float(
            self._get_property(
                CAP_PROP_FPS
            )
        )

    def get_current_position_in_milliseconds(
        self
    ):
        return float(
            self._get_property(
                CAP_PROP_POS_MSEC
            )
        )

    def get_current_position_by_frames(
            self
    ):
        return int(
            self._get_property(
                CAP_PROP_POS_FRAMES
            )
        )

    def get_bitrate(
        self
    ):
        return float(
            self._get_property(
                CAP_PROP_BITRATE
            )
        )

    def get_total_number_of_frames(
            self
    ):
        return int(
            self._get_property(
                CAP_PROP_FRAME_COUNT
            )
        )

    def get_convert_to_rgb(
        self
    ):
        return bool(
            self._get_property(
                CAP_PROP_CONVERT_RGB
            )
        )

    def _get_property(
            self,
            property_to_retrieve: int
    ):
        return self.get_stream()    \
            .get_capture_device()   \
            .get(
            property_to_retrieve
        )
