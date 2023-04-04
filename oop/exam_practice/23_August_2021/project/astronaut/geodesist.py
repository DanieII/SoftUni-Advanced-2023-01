from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    INITIAL_OXYGEN = 50

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN)

    @property
    def oxygen_needed(self):
        return None
