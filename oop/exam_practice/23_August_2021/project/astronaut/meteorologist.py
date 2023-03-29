from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    INITIAL_OXYGEN = 90

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN)

    @property
    def additional_oxygen_needed(self):
        return 15
