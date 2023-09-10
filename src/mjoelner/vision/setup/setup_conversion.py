def setup_conversion(
    stream,
    to_type: str
):
    from mjoelner.vision.hooks \
        import StreamHookForRGB

    from mjoelner.vision \
        import VisionStreamProperties

    if to_type.lower() == '2rgb':
        stream.set_hook(
            StreamHookForRGB(
                VisionStreamProperties(
                    stream
                )
            )
        )

    from mjoelner.vision.hooks \
        import StreamOnHook

    if to_type.lower() == 'on':
        stream.set_hook(
            StreamOnHook()
        )
