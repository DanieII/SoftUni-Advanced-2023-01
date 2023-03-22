from project.movie_specification.movie import Movie


class Thriller(Movie):
    AGE = 16
    AGE_MESSAGE = "Thriller movies must be restricted for audience under 16 years!"

    def __init__(self, title, year, owner, age_restriction=16):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age(self):
        return self.AGE

    @property
    def age_message(self):
        return self.AGE_MESSAGE

    def details(self):
        return f"Thriller - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"
