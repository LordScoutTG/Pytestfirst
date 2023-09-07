from animals.animal import Animal


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __add__(self, other):
        return self.with_friend(other)

    sound = "Meow"

    def voice(self):
        if self.age % 2 == 0:
            print((self.sound + "\n") * 3)
            print("gimme fish")
        else:
            print((self.sound + "\n") * 5)
            print("gimme fish")

    def with_friend(self, friend):
        if friend.animal is Cat:
            print(f'Я {self.name} мурлыкаю с {friend.name}')
        else:
            print(f'Я {self.name} убегаю от собаки {friend.name}')
