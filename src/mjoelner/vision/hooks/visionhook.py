from abc            \
    import          \
    ABC,            \
    abstractmethod


class VisionHook(
    ABC
):
    def __init__(self):
        pass

    @abstractmethod
    def on_condition(self) -> bool:
        raise NotImplemented('not implemented method used.')
