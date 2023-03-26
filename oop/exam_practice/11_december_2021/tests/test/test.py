import unittest

from project.team import Team


class TeamTests(unittest.TestCase):

    def setUp(self) -> None:
        self.team1 = Team("TheBest")
        self.team2 = Team("TheCoolest")

    def test_constructor_for_all_attributes(self):
        self.assertEqual(self.team1.name, "TheBest")
        self.assertEqual(self.team1.members, {})

    def test_name_error(self):
        with self.assertRaises(ValueError) as error:
            self.team1.name = "12 "
        self.assertEqual(str(error.exception), "Team Name can contain only letters!")

    def test_add_member_method(self):
        expected = "Successfully added: Ivan, Mihail"
        result = self.team1.add_member(Ivan=23, Mihail=19)
        self.assertEqual(result, expected)
        self.assertEqual(self.team1.members, {"Ivan": 23, "Mihail": 19})
        self.team1.add_member(Ivan=30)
        self.assertEqual(self.team1.members, {"Ivan": 23, "Mihail": 19})

    def test_remove_member_method(self):
        self.team1.add_member(Mihail=19)
        self.assertEqual("Member Mihail removed", self.team1.remove_member("Mihail"))
        self.assertEqual(self.team1.members, {})

    def test_remove_member_method_non_existing(self):
        self.assertEqual("Member with name Vasil does not exist", self.team1.remove_member("Vasil"))

    def test_greater_method(self):
        self.team1.add_member(Vasil=35)
        self.assertTrue(self.team1 > self.team2)
        self.assertFalse(self.team2 > self.team1)

    def test_len_method(self):
        self.team1.add_member(Ivan=23)
        expected = 1
        result = len(self.team1)
        self.assertEqual(expected, result)

    def test_add_method(self):
        self.team1.add_member(Ivan=23)
        self.team2.add_member(Mihail=19, Grigor=30)

        new = self.team1 + self.team2
        self.assertEqual(new.name, "TheBestTheCoolest")
        self.assertEqual(new.members, {"Ivan": 23, "Mihail": 19, "Grigor": 30})

    def test_str_method(self):
        self.team1.add_member(Ivan=23, Georgi=30, Grigor=30)
        expected = "Team name: TheBest\n" \
                   "Member: Georgi - 30-years old\n" \
                   "Member: Grigor - 30-years old\n" \
                   "Member: Ivan - 23-years old"
        result = str(self.team1)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
