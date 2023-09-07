from animals.cat import Cat
from animals.dog import Dog

if __name__ == "__main__":

    cat = Cat("Barsik", 35)
    kitty = Cat("Bonya", 21)
    dog = Dog("Alba", 12)
    cat.with_friend(dog)
    dog.voice()
    kitty.voice()
    cat + kitty
