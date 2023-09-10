from mjoelner.vision \
    import VisionStream

from random \
    import SystemRandom

location_of_video: str = 'C:\\Users\\Kentv\\Videos\\Halo  The Master Chief Collection\\Halo  The Master Chief Collection 2023.09.10 - 13.33.16.03.mp4'


def generate_vision_stream() -> VisionStream:
    global location_of_video
    return VisionStream(
        location_of_video
    )


def generate_vision_stream_move_to(r_start: int = 5, r_end: int = 200) -> VisionStream:
    stream = generate_vision_stream()

    counter: int = 0

    end_counter_at: int = SystemRandom().randint(
        r_start,
        r_end
    )

    while stream.is_open():
        counter = counter + 1

        stream.capture()

        if counter >= end_counter_at:
            break

    return stream
