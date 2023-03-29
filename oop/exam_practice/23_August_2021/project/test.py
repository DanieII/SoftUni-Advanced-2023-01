import unittest

from project.space_station import SpaceStation


class TestProject(unittest.TestCase):

    def setUp(self) -> None:
        self.space_station = SpaceStation()

    def test_add_astronaut(self):
        result = self.space_station.add_astronaut("Biologist", "ProfessionalBiologist")
        self.assertEqual(result, "Successfully added Biologist: ProfessionalBiologist.")
        self.assertEqual(len(self.space_station.astronaut_repository.astronauts), 1)

    def test_add_planet(self):
        result = self.space_station.add_planet("Saturn", "flashlight, shovel, flag")
        self.assertEqual(result, "Successfully added Planet: Saturn.")
        self.assertEqual(len(self.space_station.planet_repository.planets), 1)

    def test_send_on_mission(self):
        self.space_station.add_astronaut("Biologist", "ProfessionalBiologist")
        self.space_station.add_planet("Saturn", "flashlight")
        print(self.space_station.send_on_mission("Saturn"))


if __name__ == '__main__':
    unittest.main()
