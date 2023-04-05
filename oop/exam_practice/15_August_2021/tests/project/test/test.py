import unittest

from project.pet_shop import PetShop


class TestPetShop(unittest.TestCase):

    def setUp(self) -> None:
        self.shop = PetShop("Vitosha")

    def test_constructor(self):
        assert self.shop.name == "Vitosha"
        assert self.shop.food == {}
        assert self.shop.pets == []

    def test_add_food_invalid_quantity_error(self):
        with self.assertRaises(ValueError) as error:
            self.shop.add_food("dog food", -1)
        assert str(error.exception) == 'Quantity cannot be equal to or less than 0'

    def test_add_food_successful(self):
        result = self.shop.add_food("dog food", 10)
        assert result == "Successfully added 10.00 grams of dog food."
        assert self.shop.food["dog food"] == 10
        self.shop.add_food("dog food", 1)
        assert self.shop.food["dog food"] == 11

    def test_add_pet_successful(self):
        result = self.shop.add_pet("Riley")
        self.shop.add_pet("Buck")
        assert result == "Successfully added Riley."
        assert self.shop.pets == ["Riley", "Buck"]

    def test_add_pet_with_same_name(self):
        self.shop.add_pet("Riley")
        with self.assertRaises(Exception) as error:
            self.shop.add_pet("Riley")
        assert str(error.exception) == "Cannot add a pet with the same name"

    def test_feed_pet_without_a_valid_name(self):
        with self.assertRaises(Exception) as error:
            self.shop.feed_pet("dog food", "Riley")
        assert str(error.exception) == "Please insert a valid pet name"

    def test_feed_pet_without_a_valid_food(self):
        self.shop.add_pet("Riley")
        result = self.shop.feed_pet("dog food", "Riley")
        assert result == 'You do not have dog food'

    def test_feed_pet_add_additional_food(self):
        self.shop.add_pet("Riley")
        self.shop.add_food("dog food", 10)
        result = self.shop.feed_pet("dog food", "Riley")
        assert result == "Adding food..."
        assert self.shop.food["dog food"] == 1010

    def test_feed_pet_successful(self):
        self.shop.add_pet("Riley")
        self.shop.add_food("dog food", 200)
        result = self.shop.feed_pet("dog food", "Riley")
        assert result == "Riley was successfully fed"
        assert self.shop.food["dog food"] == 100

    def test_repr(self):
        self.shop.add_pet("Riley")
        self.shop.add_pet("Buck")
        expected = f'Shop Vitosha:\n' \
                   f'Pets: Riley, Buck'
        assert self.shop.__repr__() == expected


if __name__ == '__main__':
    unittest.main()
