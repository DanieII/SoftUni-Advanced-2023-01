import unittest

from project.shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):

    def setUp(self) -> None:
        self.cart = ShoppingCart("Billa", 100)

    def test_constructor(self):
        assert self.cart.shop_name == "Billa"
        assert self.cart.budget == 100
        assert self.cart.products == {}

    def test_shop_name_not_uppercase_error(self):
        with self.assertRaises(ValueError) as error:
            self.cart.shop_name = "billa"
        assert str(error.exception) == "Shop must contain only letters and must start with capital letter!"

    def test_shop_name_not_alpha_error(self):
        with self.assertRaises(ValueError) as error:
            self.cart.shop_name = "6"
        assert str(error.exception) == "Shop must contain only letters and must start with capital letter!"

    def test_add_to_cart_cost_too_much(self):
        with self.assertRaises(ValueError) as error:
            self.cart.add_to_cart("fan", 101)
        assert str(error.exception) == "Product fan cost too much!"

    def test_add_to_cart_successful(self):
        result = self.cart.add_to_cart("cola", 3)
        assert result == "cola product was successfully added to the cart!"
        assert self.cart.products["cola"] == 3

    def test_remove_from_cart_no_product(self):
        with self.assertRaises(ValueError) as error:
            self.cart.remove_from_cart("gum")
        assert str(error.exception) == "No product with name gum in the cart!"

    def test_remove_from_cart_successful(self):
        self.cart.add_to_cart("cola", 3)
        self.cart.add_to_cart("fanta", 3)
        result = self.cart.remove_from_cart("cola")
        assert result == "Product cola was successfully removed from the cart!"
        assert self.cart.products == {"fanta": 3}

    def test_add(self):
        self.cart.add_to_cart("cola", 3)
        self.cart.add_to_cart("fanta", 3)
        other = ShoppingCart("Other", 50)
        other.add_to_cart("fan", 15)
        other.add_to_cart("ketchup", 5)
        new = self.cart + other
        assert new.shop_name == "BillaOther"
        assert new.budget == 150
        assert list(new.products) == ["cola", "fanta", "fan", "ketchup"]
        assert new.products == {"cola": 3, "fanta": 3, "fan": 15, "ketchup": 5}

    def test_buy_products_not_enough_money(self):
        self.cart.add_to_cart("cola", 60)
        self.cart.add_to_cart("fan", 50)
        with self.assertRaises(ValueError) as error:
            self.cart.buy_products()
        assert str(error.exception) == "Not enough money to buy the products! Over budget with 10.00lv!"

    def test_buy_products_successful(self):
        self.cart.add_to_cart("cola", 50)
        self.cart.add_to_cart("fan", 49)
        result = self.cart.buy_products()
        assert result == 'Products were successfully bought! Total cost: 99.00lv.'


if __name__ == '__main__':
    unittest.main()
