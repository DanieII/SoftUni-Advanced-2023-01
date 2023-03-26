from project.car.car import Car


class MuscleCar(Car):
    MINIMUM = 250
    MAXIMUM = 450

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        minimum, maximum = self.MINIMUM, self.MAXIMUM
        if not minimum <= value <= maximum:
            raise ValueError(f"Invalid speed limit! Must be between {minimum} and {maximum}!")
        self.__speed_limit = value
