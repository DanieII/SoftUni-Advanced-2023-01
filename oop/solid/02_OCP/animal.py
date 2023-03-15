def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


class Cat:

    def make_sound(self):
        return 'meow'


class Dog:

    def make_sound(self):
        return 'woof-woof'


animals = [Cat(), Dog()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
