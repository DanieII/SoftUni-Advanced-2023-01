from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    @staticmethod
    def __get_object_from_attribute(attribute, value, collection):
        for o in collection:
            if getattr(o, attribute) == value:
                return o

    @staticmethod
    def check_if_user_owns_the_movie(user, movie):
        if user != movie.owner:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

    def check_if_movie_is_uploaded(self, movie):
        if not self.__get_object_from_attribute("title", movie.title, self.movies_collection):
            raise Exception(f"The movie {movie.title} is not uploaded!")

    def register_user(self, username: str, age: int):
        if self.__get_object_from_attribute("username", username, self.users_collection):
            raise Exception("User already exists!")

        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.__get_object_from_attribute("username", username, self.users_collection)
        if not user:
            raise Exception("This user does not exist!")

        self.check_if_user_owns_the_movie(user, movie)

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.__get_object_from_attribute("username", username, self.users_collection)

        self.check_if_movie_is_uploaded(movie)
        self.check_if_user_owns_the_movie(user, movie)

        for attribute, value in kwargs.items():
            movie.__dict__[f"_Movie__{attribute}"] = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.__get_object_from_attribute("username", username, self.users_collection)

        self.check_if_movie_is_uploaded(movie)
        self.check_if_user_owns_the_movie(user, movie)

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__get_object_from_attribute("username", username, self.users_collection)

        if user == movie.owner:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        # if self.__get_object_from_attribute("title", movie.title, user.movies_owned):
        #     raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        # if self.__get_object_from_attribute("title", movie.title, user.movies_liked):
        #     raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__get_object_from_attribute("username", username, self.users_collection)

        if not self.__get_object_from_attribute("title", movie.title, user.movies_liked):
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        result = [x.details() for x in sorted_movies]

        return "\n".join(result)

    def __str__(self):
        result = []

        if not self.users_collection:
            result.append("All users: No users.")
        else:
            result.append(f"All users: {', '.join([x.username for x in self.users_collection])}")

        if not self.movies_collection:
            result.append("All movies: No movies.")
        else:
            result.append(f"All movies: {', '.join([x.title for x in self.movies_collection])}")

        return "\n".join(result)
