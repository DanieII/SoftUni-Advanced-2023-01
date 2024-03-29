from abc import ABC, abstractmethod
from project.user import User


class Movie(ABC):

    def __init__(self, title: str, year: int, owner: User, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    @abstractmethod
    def age(self):
        pass

    @property
    @abstractmethod
    def age_message(self):
        pass

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("The title cannot be empty string!")

        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")

        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")

        self.__owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if int(value) < self.age:
            raise ValueError(self.age_message)

        self.__age_restriction = int(value)

    @abstractmethod
    def details(self):
        pass
