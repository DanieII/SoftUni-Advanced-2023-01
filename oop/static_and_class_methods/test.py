import unittest

from shop import Shop


class ShopTests(unittest.TestCase):
    def setUp(self):
        self.fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)

    def test_add_item_success(self):
        result = self.fresh_shop.add_item("Bananas")
        self.assertEqual(self.fresh_shop.items["Bananas"], 1)
        self.assertEqual(result, "Bananas added to the shop")

    def test_remove_item_success(self):
        self.fresh_shop.add_item("Bananas")
        result = self.fresh_shop.remove_item("Bananas", 1)
        self.assertEqual(result, "1 Bananas removed from the shop")

    def test_remove_item_unsuccessful(self):
        self.fresh_shop.add_item("Bananas")
        result = self.fresh_shop.remove_item("Tomatoes", 2)
        self.assertEqual(result, "Cannot remove 2 Tomatoes")

    def test_repr(self):
        self.assertEqual(repr(self.fresh_shop), "Fresh Shop of type Fruit and Veg with capacity 50")


if __name__ == "__main__":
    unittest.main()
