from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    @property
    def available_musicians(self):
        return {
            "Guitarist": Guitarist,
            "Drummer": Drummer,
            "Singer": Singer
        }

    @staticmethod
    def __get_object_from_attribute(attribute, value, iterable):
        for obj in iterable:
            if getattr(obj, attribute) == value:
                return obj

    @staticmethod
    def __check_for_needed_types_of_musicians(band):
        all_musician_types_in_band = [x.__class__.__name__ for x in band.members]
        if len(set(all_musician_types_in_band)) < 3:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

    @staticmethod
    def __check_collection_for_skill(skill: str, collection: list):
        for i in collection:
            if skill not in i.skills:
                return False
        return True

    def __check_band_for_needed_skills(self, genre, band: Band):
        valid = False
        drummers = [x for x in band.members if x.__class__.__name__ == "Drummer"]
        singers = [x for x in band.members if x.__class__.__name__ == "Singer"]
        guitarists = [x for x in band.members if x.__class__.__name__ == "Guitarist"]
        if genre == "Rock":
            valid = all((self.__check_collection_for_skill("play the drums with drumsticks", drummers),
                         self.__check_collection_for_skill("sing high pitch notes", singers),
                         self.__check_collection_for_skill("play rock", guitarists)))
        elif genre == "Metal":
            valid = all((self.__check_collection_for_skill("play the drums with drumsticks", drummers),
                         self.__check_collection_for_skill("sing low pitch notes", singers),
                         self.__check_collection_for_skill("play metal", guitarists)))
        elif genre == 'Jazz':
            valid = all((self.__check_collection_for_skill("play the drums with drum brushes", drummers),
                         self.__check_collection_for_skill("sing high pitch notes", singers),
                         self.__check_collection_for_skill("sing low pitch notes", singers),
                         self.__check_collection_for_skill("play jazz", guitarists)))
        if not valid:
            raise Exception(f"The {band.name} band is not ready to play at the concert!")

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.available_musicians:
            raise ValueError("Invalid musician type!")
        if self.__get_object_from_attribute("name", name, self.musicians):
            raise Exception(f"{name} is already a musician!")

        musician = self.available_musicians[musician_type](name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if self.__get_object_from_attribute("name", name, self.bands):
            raise Exception(f"{name} band is already created!")

        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self.__get_object_from_attribute("place", place, self.concerts)
        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.__get_object_from_attribute("name", musician_name, self.musicians)
        band: Band = self.__get_object_from_attribute("name", band_name, self.bands)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band: Band = self.__get_object_from_attribute("name", band_name, self.bands)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = self.__get_object_from_attribute("name", musician_name, band.members)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self.__get_object_from_attribute("name", band_name, self.bands)
        concert = self.__get_object_from_attribute("place", concert_place, self.concerts)
        genre = concert.genre

        self.__check_for_needed_types_of_musicians(band)
        self.__check_band_for_needed_skills(genre, band)

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {genre} concert in {concert_place}."
