from template.stream_object \
    import generate_vision_stream


def test_stream_can_open():
    vs = generate_vision_stream()
    image = vs.capture()
    assert True


