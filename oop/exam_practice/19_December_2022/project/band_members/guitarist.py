from project.band_members.musician import Musician


class Guitarist(Musician):
    AVAILABLE = ["play metal", "play rock", "play jazz"]

    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def available_skills(self):
        return self.AVAILABLE
