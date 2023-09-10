def setup_conversion(
    stream,
    to_type: str
):

    if to_type.lower() == '2rgb':
        stream.set_hook(
            generate_rgb_hook(
                stream
            )
        )

    if to_type.lower() == 'on':
        stream.set_hook(
            generate_on_hook()
        )


def generate_rgb_hook(
    stream
):
    from mjoelner.vision.hooks \
        import StreamHookForRGB

    hook = StreamHookForRGB(
        generate_vision_properties_for_stream(
            stream
        )
    )

    return hook


def generate_on_hook():
    from mjoelner.vision.hooks \
        import StreamOnHook

    return StreamOnHook()


def generate_vision_properties_for_stream(
    stream
):
    from mjoelner.vision.properties \
        import VisionStreamProperties

    return VisionStreamProperties(
        stream
    )
