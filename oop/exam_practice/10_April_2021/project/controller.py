from typing import List

from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    AVAILABLE_AQUARIUMS = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium
    }
    AVAILABLE_DECORATIONS = {
        "Ornament": Ornament,
        "Plant": Plant
    }
    AVAILABLE_FISH = {
        "FreshwaterFish": FreshwaterFish,
        "SaltwaterFish": SaltwaterFish
    }

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: List[BaseAquarium] = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.AVAILABLE_AQUARIUMS:
            return "Invalid aquarium type."

        aquarium = self.AVAILABLE_AQUARIUMS[aquarium_type](aquarium_name)
        self.aquariums.append(aquarium)

        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.AVAILABLE_DECORATIONS:
            return f"Invalid decoration type."

        decoration = self.AVAILABLE_DECORATIONS[decoration_type]()
        self.decorations_repository.add(decoration)

        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquariums = [x for x in self.aquariums if x.name == aquarium_name]
        decorations = [x for x in self.decorations_repository.decorations if x.__class__.__name__ == decoration_type]

        if not decorations:
            return f"There isn't a decoration of type {decoration_type}."

        if aquariums:
            aquarium = aquariums[0]
            decoration = decorations[0]

            self.decorations_repository.decorations.remove(decoration)
            aquarium.add_decoration(decoration)

            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.AVAILABLE_FISH:
            return f"There isn't a fish of type {fish_type}."

        aquarium = [x for x in self.aquariums if x.name == aquarium_name][0]

        if aquarium.capacity == len(aquarium.fish):
            return "Not enough capacity."

        if fish_type[:3] != aquarium.__class__.__name__[:3]:
            return "Water not suitable."

        fish = self.AVAILABLE_FISH[fish_type](fish_name, fish_species, price)
        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = [x for x in self.aquariums if x.name == aquarium_name][0]
        aquarium.feed()

        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = [x for x in self.aquariums if x.name == aquarium_name][0]

        value = 0
        value += sum(x.price for x in aquarium.fish)
        value += sum(x.price for x in aquarium.decorations)

        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        output = [str(x) for x in self.aquariums]

        return "\n".join(output)
