from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    @abstractmethod
    def processors(self):
        pass

    @property
    @abstractmethod
    def max_ram(self):
        pass

    @property
    @abstractmethod
    def product(self):
        pass

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @property
    def available_ram(self):
        ram = []
        current = 2

        while current <= self.max_ram:
            ram.append(current)
            current *= 2

        return ram

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.processors:
            raise ValueError(f"{processor} is not compatible with {self.product} {self.manufacturer} {self.model}!")

        if ram not in self.available_ram or ram > self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.product} {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram

        self.price = self.processors[processor] + int(log2(ram) * 100)

        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
