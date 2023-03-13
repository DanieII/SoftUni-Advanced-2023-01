from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):
    FOOD = [Vegetable, Fruit]

    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def specific_food(self):
        return self.FOOD

    @property
    def animal_weight_increase(self):
        return 0.10


class Dog(Mammal):
    FOOD = [Meat]

    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def specific_food(self):
        return self.FOOD

    @property
    def animal_weight_increase(self):
        return 0.40


class Cat(Mammal):
    FOOD = [Vegetable, Meat]

    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def specific_food(self):
        return self.FOOD

    @property
    def animal_weight_increase(self):
        return 0.30


class Tiger(Mammal):
    FOOD = [Meat]

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def specific_food(self):
        return self.FOOD

    @property
    def animal_weight_increase(self):
        return 1.00
