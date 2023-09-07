from animals.animal import Animal


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.count = 0

    def __add__(self, other):
        return self.with_friend(other)

    def __call__(self):
        self.count += 1
        return self.count

    sound = "Meow"

    def voice(self):
        self.count += 1
        if self.age % 2 == 0:
            if self.count <= 3:
                print(self.sound)
            else:
                print("gimme fish")
        else:
            if self.count <= 5:
                print(self.sound)
            else:
                print("gimme fish")

    def with_friend(self, friend):
        if friend.animal is Cat:
            print(f'Я {self.name} мурлыкаю с {friend.name}')
        else:
            print(f'Я {self.name} убегаю от собаки {friend.name}')

