import unittest

from project.tennis_player import TennisPlayer


class TestTennisPlayer(unittest.TestCase):

    def setUp(self) -> None:
        self.player = TennisPlayer("Ivan", 20, 80)

    def test_constructor(self):
        self.assertEqual(self.player.name, "Ivan")
        self.assertEqual(self.player.age, 20)
        self.assertEqual(self.player.points, 80)
        self.assertEqual(self.player.wins, [])

    def test_name_error_with_2(self):
        with self.assertRaises(ValueError) as error:
            self.player.name = "Iv"
        self.assertEqual(str(error.exception), "Name should be more than 2 symbols!")

    def test_name_error_with_less_than_2(self):
        with self.assertRaises(ValueError) as error:
            self.player.name = "I"
        self.assertEqual(str(error.exception), "Name should be more than 2 symbols!")

    def test_age_error(self):
        with self.assertRaises(ValueError) as error:
            self.player.age = 17
        self.assertEqual(str(error.exception), "Players must be at least 18 years of age!")

    def test_add_new_win_successful(self):
        self.player.add_new_win("SoftUni")
        self.assertEqual(self.player.wins, ["SoftUni"])

    def test_add_new_win_already_added(self):
        self.player.add_new_win("SoftUni")
        self.player.add_new_win("Golf")
        result = self.player.add_new_win("SoftUni")
        self.assertEqual(result, "SoftUni has been already added to the list of wins!")
        self.assertEqual(self.player.wins, ["SoftUni", "Golf"])

    def test_less_than(self):
        other = TennisPlayer("Grigor", 30, 100)
        result = self.player < other
        self.assertEqual(result, 'Grigor is a top seeded player and he/she is better than Ivan')
        result2 = other < self.player
        self.assertEqual(result2, 'Grigor is a better player than Ivan')

    def test_str(self):
        self.player.add_new_win("SoftUni")
        self.player.add_new_win("Golf")
        expected = f"Tennis Player: Ivan\n" \
                   f"Age: 20\n" \
                   f"Points: 80.0\n" \
                   f"Tournaments won: SoftUni, Golf"
        self.assertEqual(str(self.player), expected)


if __name__ == '__main__':
    unittest.main()
