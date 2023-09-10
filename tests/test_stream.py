from mjoelner.vision \
    import VisionStream, VisionStreamProperties

location_of_video: str = 'C:\\Users\\Kentv\\Videos\\Halo  The Master Chief Collection\\Halo  The Master Chief Collection 2023.09.10 - 13.33.16.03.mp4'


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
    properties = VisionStreamProperties(vs)
    counter = 0

    while vs.is_open():
        counter = counter + 1
        vs.capture()

        if counter >= 500:
            break

    print()
    print(
        'width: ',
        properties.get_frame_width()
    )

    print(
        'height: ',
        properties.get_frame_height()
    )

    print(
        'total number of frames: ',
        properties.get_total_number_of_frames()
    )

    print(
        'should convert: ',
        properties.get_convert_to_rgb()
    )

    print(
        'fps: ',
        properties.get_frames_per_second()
    )

    print(
        'current position: ',
        properties.get_current_position()
    )




