import unittest

from project.toy_store import ToyStore


class TestToyStore(unittest.TestCase):

    def setUp(self) -> None:
        self.store = ToyStore()

    def test_constructor(self):
        assert self.store.toy_shelf == {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

    def test_add_toy_shelf_doesnt_exist(self):
        with self.assertRaises(Exception) as error:
            self.store.add_toy("Z", "car")
        assert str(error.exception) == "Shelf doesn't exist!"

    def test_add_toy_toy_already_in_shelf(self):
        self.store.toy_shelf["A"] = "car"
        with self.assertRaises(Exception) as error:
            self.store.add_toy("A", "car")
        assert str(error.exception) == "Toy is already in shelf!"

    def test_add_toy_shelf_already_taken(self):
        self.store.toy_shelf["A"] = "car"
        with self.assertRaises(Exception) as error:
            self.store.add_toy("A", "bear")
        assert str(error.exception) == "Shelf is already taken!"

    def test_add_toy_successful(self):
        result = self.store.add_toy("A", "car")
        assert result == "Toy:car placed successfully!"
        assert self.store.toy_shelf["A"] == "car"

    def test_remove_toy_shelf_doesnt_exist(self):
        with self.assertRaises(Exception) as error:
            self.store.remove_toy("Z", "car")
        assert str(error.exception) == "Shelf doesn't exist!"

    def test_remove_toy_doesnt_exist(self):
        with self.assertRaises(Exception) as error:
            self.store.remove_toy("A", "car")
        assert str(error.exception) == "Toy in that shelf doesn't exists!"

    def test_remove_toy_successful(self):
        self.store.add_toy("A", "car")
        result = self.store.remove_toy("A", "car")
        assert result == "Remove toy:car successfully!"
        assert self.store.toy_shelf["A"] is None


if __name__ == '__main__':
    unittest.main()
