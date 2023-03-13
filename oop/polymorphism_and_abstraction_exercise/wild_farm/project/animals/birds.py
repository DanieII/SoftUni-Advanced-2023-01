from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    FOOD = [Meat]

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def specific_food(self):
        return self.FOOD

    @property
    def animal_weight_increase(self):
        return 0.25


class Hen(Bird):
    FOOD = [Vegetable, Fruit, Meat, Seed]

    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def specific_food(self):
        return self.FOOD

    @property
    def animal_weight_increase(self):
        return 0.35
