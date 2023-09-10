from mjoelner.vision.adapters.pillow_adapter \
    import VisionAdapterForPillow

from template.stream_object \
    import generate_vision_stream_move_to


def test_adapter_for_pillow():
    stream = generate_vision_stream_move_to()
    adapter = VisionAdapterForPillow(stream)

    image = adapter.retrieve_image_as()
    image.save('D:\\Screenshot\\test.jpg')

    assert True
