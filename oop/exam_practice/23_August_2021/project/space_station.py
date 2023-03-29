from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.not_completed_missions = 0

    @staticmethod
    def __get_object_from_attribute(attribute, value, collection):
        for o in collection:
            if getattr(o, attribute) == value:
                return o

    @staticmethod
    def start_mission(planet: Planet, astronauts_sent):
        while True:
            if not planet.items:
                return True
            if not astronauts_sent:
                return False

            current_astronaut = astronauts_sent.pop(0)

            while current_astronaut.oxygen > 0 and planet.items:
                planet.items.pop()
                current_astronaut.breathe()

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.__get_object_from_attribute("name", name, self.astronaut_repository.astronauts):
            return f"{name} is already added."

        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")

        if astronaut_type == "Biologist":
            astronaut = Biologist(name)
        elif astronaut_type == "Geodesist":
            astronaut = Geodesist(name)
        elif astronaut_type == "Meteorologist":
            astronaut = Meteorologist(name)

        self.astronaut_repository.astronauts.append(astronaut)

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.__get_object_from_attribute("name", name, self.planet_repository.planets):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items.extend(items.split(", "))

        self.planet_repository.planets.append(planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.__get_object_from_attribute("name", name, self.astronaut_repository.astronauts)

        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.astronauts.remove(astronaut)

        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.__get_object_from_attribute("name", planet_name, self.planet_repository.planets)

        if not planet:
            raise Exception("Invalid planet name!")

        astronauts_with_more_than_30_units = list(filter(lambda x: x.oxygen > 30, self.astronaut_repository.astronauts))

        if not astronauts_with_more_than_30_units:
            f"You need at least one astronaut to explore the planet!"

        astronauts_sorted_in_descending_order_by_units = sorted(astronauts_with_more_than_30_units,
                                                                key=lambda x: -x.oxygen)

        astronauts = []

        for astronaut in astronauts_sorted_in_descending_order_by_units:
            if len(astronauts) < 5:
                astronauts.append(astronaut)

        number_of_astronauts = len(astronauts)

        completed = self.start_mission(planet, astronauts)

        if completed:
            self.successful_missions += 1
            return f"Planet: {planet_name} was explored. {number_of_astronauts} astronauts participated in collecting items."

        self.not_completed_missions += 1
        return "Mission is not completed."

    def report(self):
        result = [f"{self.successful_missions} successful missions!",
                  f"{self.not_completed_missions} missions were not completed!", "Astronauts' info:"]
        for astronaut in self.astronaut_repository.astronauts:
            result.append(f"Name: {astronaut.name}")
            result.append(f"Oxygen: {astronaut.oxygen}")
            if astronaut.backpack:
                result.append(f"Backpack items: {', '.join(astronaut.backpack)}")
            else:
                result.append(f"Backpack items: none")

        return "\n".join(result)
