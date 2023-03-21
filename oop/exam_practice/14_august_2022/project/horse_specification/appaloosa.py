from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAXIMUM_SPEED = 120
    SPEED_INCREASE = 2

    @property
    def maximum_speed(self):
        return self.MAXIMUM_SPEED

    @property
    def speed_increase(self):
        return self.SPEED_INCREASE
