from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAXIMUM_SPEED = 140
    SPEED_INCREASE = 3

    @property
    def maximum_speed(self):
        return self.MAXIMUM_SPEED

    @property
    def speed_increase(self):
        return self.SPEED_INCREASE
