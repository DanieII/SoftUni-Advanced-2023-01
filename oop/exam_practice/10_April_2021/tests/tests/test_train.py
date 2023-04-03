import unittest

from project.train.train import Train


class TestTrain(unittest.TestCase):

    def setUp(self) -> None:
        self.train = Train("Fastest", 100)

    def test_class_attributes(self):
        assert self.train.TRAIN_FULL == "Train is full"
        assert self.train.PASSENGER_EXISTS == "Passenger {} Exists"
        assert self.train.PASSENGER_NOT_FOUND == "Passenger Not Found"
        assert self.train.PASSENGER_ADD == "Added passenger {}"
        assert self.train.PASSENGER_REMOVED == "Removed {}"
        assert self.train.ZERO_CAPACITY == 0

    def test_constructor(self):
        assert self.train.name == "Fastest"
        assert self.train.capacity == 100
        assert self.train.passengers == []

    def test_add_full_error(self):
        self.train.capacity = 1
        self.train.passengers = ["Ivan"]
        with self.assertRaises(ValueError) as error:
            self.train.add("Gosho")
        assert str(error.exception) == "Train is full"

    def test_add_same_name(self):
        self.train.passengers = ["Ivan"]
        with self.assertRaises(ValueError) as error:
            self.train.add("Ivan")
        assert str(error.exception) == "Passenger Ivan Exists"

    def test_add_successful(self):
        result = self.train.add("Ivan")
        assert self.train.passengers == ["Ivan"]
        assert result == "Added passenger Ivan"

    def test_remove_non_existing(self):
        with self.assertRaises(ValueError) as error:
            self.train.remove("Ivan")
        assert str(error.exception) == "Passenger Not Found"

    def test_remove_successful(self):
        self.train.add("Ivan")
        result = self.train.remove("Ivan")
        assert result == "Removed Ivan"
        assert self.train.passengers == []


if __name__ == "__main__":
    unittest.main()
