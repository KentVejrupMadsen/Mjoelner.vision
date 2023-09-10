from mjoelner.vision.adapters.pillow_adapter \
    import VisionAdapterForPillow

from template.stream_object \
    import generate_vision_stream_move_to, generate_vision_stream


def test_adapter_for_pillow():
    stream = generate_vision_stream_move_to()
    adapter = VisionAdapterForPillow(stream)

    image = adapter.retrieve_image_as()
    image.save('D:\\Screenshot\\test.jpg')

    assert True


def test_adapter_for_pillow_stream_not_started():
    stream = generate_vision_stream()
    adapter = VisionAdapterForPillow(stream)

    image = adapter.retrieve_image_as()
    image.save('D:\\Screenshot\\test2.jpg')

    assert True
