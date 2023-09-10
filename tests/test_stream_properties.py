from template.stream_object \
    import generate_vision_stream_move_to

from mjoelner.vision.properties.stream_properties \
    import VisionStreamProperties


def test_stream_properties():
    vs = generate_vision_stream_move_to()

    properties = VisionStreamProperties(
        vs
    )

    assert True