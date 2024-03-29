from project.planet.planet import Planet


class PlanetRepository:

    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        self.planets.remove(planet)

    def find_by_name(self, name: str):
        try:
            planet = [x for x in self.planets if x.name == name][0]
        except IndexError:
            return None
        return planet
