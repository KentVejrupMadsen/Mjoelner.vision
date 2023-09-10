from mjoelner.vision.hooks.hook \
    import Hook


class StreamOnHook(
    Hook
):
    def __init__(self):
        super().__init__()
        self.value: bool = True

    def on_condition(
        self
    ) -> bool:
        return self.get_value()

    def get_value(
        self
    ) -> bool:
        return self.value

    def set_value(
        self,
        value: bool
    ) -> None:
        self.value = value
