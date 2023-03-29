from abc import ABC, abstractmethod


class Astronaut(ABC):
    ASTRONAUT_OXYGEN_DECREASE_PER_BREATH = 10

    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @property
    @abstractmethod
    def additional_oxygen_needed(self):
        pass

    def breathe(self):
        current_needed_for_breath = self.ASTRONAUT_OXYGEN_DECREASE_PER_BREATH
        if self.additional_oxygen_needed:
            current_needed_for_breath += self.additional_oxygen_needed

        self.oxygen -= current_needed_for_breath

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
