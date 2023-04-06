import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):

    def setUp(self) -> None:
        self.factory = PaintFactory("Rainbow", 100)

    def test_constructor(self):
        assert self.factory.name == "Rainbow"
        assert self.factory.capacity == 100
        assert self.factory.ingredients == {}
        assert self.factory.valid_ingredients == ["white", "yellow", "blue", "green", "red"]

    def test_can_add(self):
        self.factory.ingredients = {"white": 10, "yellow": 20}
        result = self.factory.can_add(71)
        assert result is False

    def test_add_ingredient_not_in_valid(self):
        with self.assertRaises(TypeError) as error:
            self.factory.add_ingredient("orange", 10)
        assert str(error.exception) == "Ingredient of type orange not allowed in PaintFactory"

    def test_add_ingredient_not_enough_space(self):
        with self.assertRaises(ValueError) as error:
            self.factory.add_ingredient("white", 101)
        assert str(error.exception) == "Not enough space in factory"

    def test_add_ingredient_successful(self):
        self.factory.add_ingredient("white", 10)
        assert self.factory.ingredients["white"] == 10
        self.factory.add_ingredient("white", 20)
        assert self.factory.ingredients["white"] == 30

    def test_remove_ingredient_no_such_ingredient(self):
        with self.assertRaises(KeyError) as error:
            self.factory.remove_ingredient("orange", 10)
        assert str(error.exception) == "'No such ingredient in the factory'"

    def test_remove_ingredient_cannot_be_less_than_zero(self):
        self.factory.add_ingredient("white", 10)
        with self.assertRaises(ValueError) as error:
            self.factory.remove_ingredient("white", 11)
        assert str(error.exception) == "Ingredients quantity cannot be less than zero"

    def test_remove_ingredient_successful(self):
        self.factory.add_ingredient("white", 10)
        self.factory.remove_ingredient("white", 9)
        assert self.factory.ingredients["white"] == 1

    def test_products_property(self):
        self.factory.add_ingredient("white", 10)
        assert self.factory.products == self.factory.ingredients

    def test_repr(self):
        self.factory.add_ingredient("white", 10)
        self.factory.add_ingredient("yellow", 11)
        expected = f"Factory name: Rainbow with capacity 100.\n" \
                   f"white: 10\n" \
                   f"yellow: 11\n"
        assert self.factory.__repr__() == expected


if __name__ == '__main__':
    unittest.main()
