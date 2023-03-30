import unittest

from project.team import Team


class TeamTest(unittest.TestCase):

    def setUp(self) -> None:
        self.team = Team("TheBest")

    def test_constructor(self):
        self.assertEqual(self.team.name, "TheBest")
        self.assertEqual(self.team.members, {})

    def test_name_error(self):
        with self.assertRaises(ValueError) as error:
            self.team.name = "1 "
        self.assertEqual(str(error.exception), "Team Name can contain only letters!")

    def test_add_member(self):
        self.assertEqual(self.team.add_member(Mihail=20), "Successfully added: Mihail")
        self.assertEqual(self.team.members, {"Mihail": 20})
        self.assertEqual(self.team.add_member(Georgi=25, Petar=35, Mihail=30), "Successfully added: Georgi, Petar")
        self.assertEqual(self.team.members, {"Mihail": 20, "Georgi": 25, "Petar": 35})
        self.assertEqual(len(self.team.members), 3)

    def test_add_member_with_no_new_members(self):
        self.team.members = {"Mihail": 20}
        result = self.team.add_member(Mihail=30)
        self.assertEqual(result, "Successfully added: ")
        self.assertEqual(self.team.members, {"Mihail": 20})

    def test_remove_member_successful(self):
        self.team.members = {"Mihail": 20, "Kaloyan": 19}
        result = self.team.remove_member("Mihail")
        self.assertEqual(result, "Member Mihail removed")
        self.assertEqual(len(self.team.members), 1)
        self.assertEqual(list(self.team.members)[0], "Kaloyan")

    def test_remove_member_not_existing(self):
        self.team.add_member(Petar=25)
        result = self.team.remove_member("Mihail")
        self.assertEqual(result, "Member with name Mihail does not exist")
        self.assertEqual(self.team.members, {"Petar": 25})

    def test_greater(self):
        other = Team("Other")
        self.team.add_member(Mihail=20)
        self.assertEqual(self.team > other, True)
        other.add_member(Georgi=21, Martin=60)
        self.assertEqual(self.team > other, False)

    def test_len(self):
        self.assertEqual(len(self.team), 0)
        self.team.add_member(Mihail=20)
        self.assertEqual(len(self.team), 1)

    def test_add(self):
        other = Team("Other")
        self.team.add_member(Petar=25)
        other.add_member(Mihail=35)
        new = self.team + other
        self.assertEqual(new.name, "TheBestOther")
        self.assertEqual(list(new.members)[0], "Petar")
        self.assertEqual(list(new.members)[1], "Mihail")

    def test_str(self):
        self.team.members = {"Grigor": 20, "Georgi": 20, "Gavril": 25}
        expected = "Team name: TheBest\n" \
                   "Member: Gavril - 25-years old\n" \
                   "Member: Georgi - 20-years old\n" \
                   "Member: Grigor - 20-years old"
        self.assertEqual(str(self.team), expected)


if __name__ == '__main__':
    unittest.main()
