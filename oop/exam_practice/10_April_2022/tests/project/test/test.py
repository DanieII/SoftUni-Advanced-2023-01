import unittest

from project.movie import Movie


class MovieTests(unittest.TestCase):

    def setUp(self) -> None:
        self.movie1 = Movie("John Wick", 2023, 7.5)
        self.movie2 = Movie("Titanic", 1997, 8.5)

    def test_constructor_for_all_attributes(self):
        self.assertEqual(self.movie1.name, "John Wick")
        self.assertEqual(self.movie1.year, 2023)
        self.assertEqual(self.movie1.rating, 7.5)
        self.assertEqual(self.movie1.actors, [])

    def test_name_error(self):
        with self.assertRaises(ValueError) as error:
            self.movie1.name = ""
        self.assertEqual(str(error.exception), "Name cannot be an empty string!")

    def test_year_error(self):
        with self.assertRaises(ValueError) as error:
            self.movie1.year = 1886
        self.assertEqual(str(error.exception), "Year is not valid!")

    def test_add_actor_method(self):
        self.movie1.add_actor("Tom Holland")
        self.assertEqual(self.movie1.actors, ["Tom Holland"])
        expected = "Tom Holland is already added in the list of actors!"
        result = self.movie1.add_actor("Tom Holland")
        self.assertEqual(result, expected)

    def test_greater_method(self):
        expected = '"Titanic" is better than "John Wick"'
        result = self.movie1 > self.movie2
        self.assertEqual(result, expected)

    def test_greater_method2(self):
        expected = '"Titanic" is better than "John Wick"'
        result = self.movie2 > self.movie1
        self.assertEqual(result, expected)

    def test_represent_method(self):
        self.movie1.add_actor("Keanu Reeves")
        self.movie1.add_actor("Donnie Yen")
        expected = f"Name: John Wick\n" \
                   f"Year of Release: 2023\n" \
                   f"Rating: 7.50\n" \
                   f"Cast: Keanu Reeves, Donnie Yen"
        result = str(self.movie1)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
