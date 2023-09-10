from template.stream_object \
    import generate_vision_stream_move_to

from mjoelner.vision.properties.stream_properties \
    import VisionStreamProperties


def no_content():
    print()


def print_values(
    key: str,
    value: str
):
    print(
        key.upper(),
        ':',
        value
    )


def test_stream_properties():
    vs = generate_vision_stream_move_to()

    properties = VisionStreamProperties(
        vs
    )

    no_content()

    print_content(
        properties
    )


def print_content(
        properties: VisionStreamProperties
):

    no_content()

    print_values(
        'bit rate',
        str(
            properties.get_bitrate()
        )
    )

    print_values(
        'width',
        str(
            properties.get_frame_width()
        )
    )

    print_values(
        'height',
        str(
            properties.get_frame_height()
        )
    )

    print_values(
        'total number of frames',
        str(
            properties.get_total_number_of_frames()
        )
    )

    print_values(
        'should convert',
        str(
            properties.get_convert_to_rgb()
        )
    )

    print_values(
        'fps',
        str(
            properties.get_frames_per_second()
        )
    )

    print_values(
        'current position',
        str(
            properties.get_current_position_by_frames()
        )
    )

    print_values(
        'current position in msec',
        str(
            properties.get_current_position_in_milliseconds()
        )
    )




