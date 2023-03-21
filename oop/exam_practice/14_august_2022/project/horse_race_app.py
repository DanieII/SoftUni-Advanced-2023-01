from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.horse_race import HorseRace
from project.horse_specification.horse import Horse


class HorseRaceApp:

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    @staticmethod
    def __get_object_from_attribute(attribute, value, collection):
        for o in collection:
            if getattr(o, attribute) == value:
                return o

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if self.__get_object_from_attribute("name", horse_name, self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type == "Appaloosa":
            self.horses.append(Appaloosa(horse_name, horse_speed))
        elif horse_type == "Thoroughbred":
            self.horses.append(Thoroughbred(horse_name, horse_speed))

        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.__get_object_from_attribute("name", jockey_name, self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self.__get_object_from_attribute("race_type", race_type, self.horse_races):
            raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey: Jockey = self.__get_object_from_attribute("name", jockey_name, self.jockeys)
        horse = [x for x in self.horses if x.__class__.__name__ == horse_type and not x.is_taken]

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        horse = horse[0]
        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race: HorseRace = self.__get_object_from_attribute("race_type", race_type, self.horse_races)
        jockey: Jockey = self.__get_object_from_attribute("name", jockey_name, self.jockeys)

        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if self.__get_object_from_attribute("name", jockey_name, horse_race.jockeys):
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race: HorseRace = self.__get_object_from_attribute("race_type", race_type, self.horse_races)

        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed = 0
        fastest_jockey = None
        for jockey in horse_race.jockeys:
            current_speed = jockey.horse.speed
            if current_speed > highest_speed:
                highest_speed = current_speed
                fastest_jockey = jockey

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {fastest_jockey.name}! " \
               f"Winner's horse: {fastest_jockey.horse.name}."
