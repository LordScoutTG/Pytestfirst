from animals.animal import Animal


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.count = 0

    def __add__(self, other):
        return self.with_friend(other)

    def __call__(self):
        self.count += 1
        return self.count

    sound = "Gav"

    def voice(self):
        self.count += 1
        if self.age % 2 == 0:
            if self.count <= 5:
                print(self.sound)
            else:
                print("gimme bone")
        else:
            if self.count <= 3:
                print(self.sound)
            else:
                print("gimme bone")

    def with_friend(self, friend):
        if friend.animal is Dog:
            print(f'Я {self.name} лаю с {friend.name}')
        else:
            print(f'Я {self.name} гонюсь за кошкой {friend.name}')