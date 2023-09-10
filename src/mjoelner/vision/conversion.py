from cv2            \
    import          \
    cvtColor,       \
    COLOR_BGR2RGB,  \
    COLOR_BGR2GRAY, \
    COLOR_BGR2RGBA


def is_label_gray(
    label: str
) -> bool:
    return label == 'gray'


def is_label_grayscale(
    label: str
) -> bool:
    return label == 'grayscale'


def is_label_bgr(
    label: str
) -> bool:
    return label == 'bgr'


def is_label_rgb(
    label: str
) -> bool:
    return label == 'rgb'


def is_label_rgba(
    label: str
) -> bool:
    return label == 'rgba'


class VisionConversion:
    def __init__(
        self,
        conversion: int = COLOR_BGR2RGB
    ):
        self.conversion_format: None | int = None

        self.set_conversion_format(
            conversion
        )

    def __del__(self):
        del self.conversion_format

    def convert(
        self,
        frame
    ):
        return cvtColor(
            frame,
            self.get_conversion_format()
        )

    def setup(
        self,
        origin_format: str,
        to_format: str
    ):
        origin = origin_format.lower()
        format_to = to_format.lower()

        if is_label_bgr(
            origin
        ):
            self.__setup_choosing_origin_bgr(
                format_to
            )

    def __setup_choosing_origin_bgr(
        self,
        to_format: str
    ):
        if is_label_rgb(
            to_format
        ):
            self.set_conversion_format(
                COLOR_BGR2RGB
            )

        if is_label_rgba(
            to_format
        ):
            self.set_conversion_format(
                COLOR_BGR2RGBA
            )

        if (
            is_label_grayscale(
                to_format
            )
            or
            is_label_gray(
                to_format
            )
        ):
            self.set_conversion_format(
                COLOR_BGR2GRAY
            )

    def get_conversion_format(
        self
    ) -> int | None:
        return self.conversion_format

    def set_conversion_format(
        self,
        value: int
    ) -> None:
        self.conversion_format = value

