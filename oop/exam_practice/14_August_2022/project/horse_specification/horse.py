from abc import ABC, abstractmethod


class Horse(ABC):

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")

        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.maximum_speed:
            raise ValueError("Horse speed is too high!")

        self.__speed = value

    @property
    @abstractmethod
    def maximum_speed(self):
        pass

    @property
    @abstractmethod
    def speed_increase(self):
        pass

    def train(self):
        if self.speed + self.speed_increase > self.maximum_speed:
            self.speed = self.maximum_speed
        else:
            self.speed += self.speed_increase
