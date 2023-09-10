from mjoelner.vision \
    import VisionStream

from mjoelner.vision.properties.stream_properties \
    import VisionStreamProperties


location_of_video: str = 'C:\\Users\\Kentv\\Videos\\Halo  The Master Chief Collection\\Halo  The Master Chief Collection 2023.09.10 - 13.33.16.03.mp4'


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


def test_stream_can_open():
    global location_of_video
    vs = VisionStream(
        location_of_video
    )
    counter = 0

    while vs.is_open():
        counter = counter + 1
        image = vs.capture()

        if counter >= 5:
            break

    assert True


def test_stream_properties():
    global location_of_video

    vs = VisionStream(
        location_of_video
    )

    properties = VisionStreamProperties(
        vs
    )

    counter = 0

    while vs.is_open():
        counter = counter + 1
        vs.capture()

        if counter >= 500:
            break

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




