import unittest

from project.plantation import Plantation


class TestPlantation(unittest.TestCase):

    def setUp(self) -> None:
        self.plantation = Plantation(100)

    def test_constructor(self):
        assert self.plantation.size == 100
        assert self.plantation.plants == {}
        assert self.plantation.workers == []

    def test_size_error(self):
        with self.assertRaises(ValueError) as error:
            self.plantation.size = -1
        assert str(error.exception) == "Size must be positive number!"

    def test_hire_worker_already_hired(self):
        self.plantation.workers = ["Ivan"]
        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker("Ivan")
        assert str(error.exception) == "Worker already hired!"

    def test_hire_worker_successful(self):
        result = self.plantation.hire_worker("Ivan")
        assert result == "Ivan successfully hired."

    def test_len(self):
        self.plantation.plants = {"Ivan": ["flower", "another flower"], "George": ["narcissus"]}
        result = len(self.plantation)
        assert result == 3

    def test_planting_worker_not_hired_error(self):
        with self.assertRaises(ValueError) as error:
            self.plantation.planting("Ivan", "flower")
        assert str(error.exception) == "Worker with name Ivan is not hired!"

    def test_planting_plantation_if_full_error(self):
        self.plantation.size = 1
        self.plantation.hire_worker("Ivan")
        self.plantation.plants = {"Ivan": ["flower"]}
        with self.assertRaises(ValueError) as error:
            self.plantation.planting("Ivan", "another flower")
        assert str(error.exception) == "The plantation is full!"

    def test_planting_not_first(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.plants = {"Ivan": ["flower"]}
        result = self.plantation.planting("Ivan", "another flower")
        assert result == "Ivan planted another flower."
        assert self.plantation.plants == {"Ivan": ["flower", "another flower"]}

    def test_planting_first(self):
        self.plantation.hire_worker("Ivan")
        result = self.plantation.planting("Ivan", "flower")
        assert result == "Ivan planted it's first flower."
        assert self.plantation.plants == {"Ivan": ["flower"]}

    def test_str(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.hire_worker("Kristian")
        self.plantation.planting("Ivan", "flower")
        self.plantation.planting("Kristian", "narcissus")
        self.plantation.planting("Kristian", "beautiful plant")
        expected = f"Plantation size: 100\n" \
                   f"Ivan, Kristian\n" \
                   f"Ivan planted: flower\n" \
                   f"Kristian planted: narcissus, beautiful plant"
        assert str(self.plantation) == expected

    def test_repr(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.hire_worker("Kristian")
        expected = "Size: 100\n" \
                   "Workers: Ivan, Kristian"
        assert self.plantation.__repr__() == expected


if __name__ == '__main__':
    unittest.main()
