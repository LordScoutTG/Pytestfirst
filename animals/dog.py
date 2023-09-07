from animals.animal import Animal


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __add__(self, other):
        return self.with_friend(other)

    sound = "Gav"

    def voice(self):
        if self.age % 2 == 0:
            print((self.sound + "\n") * 5)
            print("gimme bone")
        else:
            print((self.sound + "\n") * 3)
            print("gimme bone")

    def with_friend(self, friend):
        if friend.animal is Dog:
            print(f'Я {self.name} лаю с {friend.name}')
        else:
            print(f'Я {self.name}гонюсь за кошкой {friend.name}')