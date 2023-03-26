from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    @staticmethod
    def __get_object_from_attribute(attribute, value, collection):
        for o in collection:
            if getattr(o, attribute) == value:
                return o

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in ["MuscleCar", "SportsCar"]:

            existing_car = self.__get_object_from_attribute("model", model, self.cars)

            if existing_car:
                raise Exception(f"Car {model} is already created!")

            if car_type == "MuscleCar":
                car = MuscleCar(model, speed_limit)
            elif car_type == "SportsCar":
                car = SportsCar(model, speed_limit)

            self.cars.append(car)

            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        existing_driver = self.__get_object_from_attribute("name", driver_name, self.drivers)

        if existing_driver:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)

        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        existing_race = self.__get_object_from_attribute("name", race_name, self.races)

        if existing_race:
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__get_object_from_attribute("name", driver_name, self.drivers)

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        for car in reversed(self.cars):
            if car.__class__.__name__ == car_type and not car.is_taken:
                found_car = car
                break
        else:
            raise Exception(f"Car {car_type} could not be found!")

        if found_car:
            if driver.car:
                old_car = driver.car
                old_car.is_taken = False

                old_model = old_car.model

                driver.car = found_car
                found_car.is_taken = True

                return f"Driver {driver.name} changed his car from {old_model} to {found_car.model}."

            driver.car = found_car
            found_car.is_taken = True

            return f"Driver {driver_name} chose the car {found_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__get_object_from_attribute("name", race_name, self.races)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self.__get_object_from_attribute("name", driver_name, self.drivers)

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)

        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__get_object_from_attribute("name", race_name, self.races)

        if not race:
            f"Race {race_name} could not be found!"

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        fastest = sorted(race.drivers, key=lambda x: -x.car.speed_limit)[:3]

        for driver in fastest:
            driver.number_of_wins += 1

        result = [f"Driver {x.name} wins the {race_name} race with a speed of {x.car.speed_limit}." for x in fastest]

        return "\n".join(result)
