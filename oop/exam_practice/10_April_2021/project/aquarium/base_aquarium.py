from abc import ABC, abstractmethod

from typing import List

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: List[BaseDecoration] = []
        self.fish: List[BaseFish] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(x.comfort for x in self.decorations)

    def add_fish(self, fish: BaseFish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."

        self.fish.append(fish)

        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        output = [f"{self.name}:"]

        current_fish = ["Fish:"]
        if self.fish:
            for fish in self.fish:
                current_fish.append(fish.name)
        else:
            current_fish.append("none")
        output.append(" ".join(current_fish))

        output.append(f"Decorations: {len(self.decorations)}")
        output.append(f"Comfort: {self.calculate_comfort()}")

        return "\n".join(output)
