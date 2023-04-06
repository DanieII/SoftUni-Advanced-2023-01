import unittest

from project.truck_driver import TruckDriver


class TestTruckDriver(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = TruckDriver("Ivan", 5)

    def test_constructor(self):
        assert self.driver.name == "Ivan"
        assert self.driver.money_per_mile == 5
        assert self.driver.available_cargos == {}
        assert self.driver.earned_money == 0
        assert self.driver.miles == 0

    def test_earned_money_error(self):
        with self.assertRaises(ValueError) as error:
            self.driver.earned_money = -1
        assert str(error.exception) == "Ivan went bankrupt."

    def test_add_cargo_offer_already_added(self):
        self.driver.available_cargos["London"] = 1000
        with self.assertRaises(Exception) as error:
            self.driver.add_cargo_offer("London", 1)
        assert str(error.exception) == "Cargo offer is already added."

    def test_add_cargo_offer_successful(self):
        result = self.driver.add_cargo_offer("London", 1000)
        assert result == "Cargo for 1000 to London was added as an offer."
        assert self.driver.available_cargos["London"] == 1000

    def test_drive_best_cargo_offer_no_offers_available_error(self):
        result = self.driver.drive_best_cargo_offer()
        assert result == "There are no offers available."

    def test_drive_best_cargo_offer_successful(self):
        self.driver.add_cargo_offer("London", 1000)
        self.driver.add_cargo_offer("Munich", 2000)
        self.driver.miles = 1
        result = self.driver.drive_best_cargo_offer()
        assert result == "Ivan is driving 2000 to Munich."
        assert self.driver.miles == 2001
        assert self.driver.earned_money == 9250

    def test_check_for_activities(self):
        self.driver.earned_money = 20000
        self.driver.check_for_activities(10000)
        assert self.driver.earned_money == 8250

    def test_repr(self):
        self.driver.miles = 100000
        expected = "Ivan has 100000 miles behind his back."
        assert expected == self.driver.__repr__()


if __name__ == '__main__':
    unittest.main()
