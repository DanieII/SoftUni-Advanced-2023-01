from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    FUEL_CONSUMPTION_INCREASE = 0.9

    def drive(self, distance):
        needed = distance * (self.fuel_consumption + self.FUEL_CONSUMPTION_INCREASE)

        if self.fuel_quantity >= needed:
            self.fuel_quantity -= needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    FUEL_CONSUMPTION_INCREASE = 1.6

    def drive(self, distance):
        needed = distance * (self.fuel_consumption + self.FUEL_CONSUMPTION_INCREASE)

        if self.fuel_quantity >= needed:
            self.fuel_quantity -= needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95
