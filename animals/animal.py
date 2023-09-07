
class Animal:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def animal(self) -> object:
        return type(self)

    def voice(self) -> None:
        self.voice()

        raise NotImplementedError()


