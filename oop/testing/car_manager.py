class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)

import unittest


class CarTester(unittest.TestCase):

    def setUp(self) -> None:
        self.car = Car("something", "X", 5, 15)

    def test_constructor(self):
        self.assertEqual(self.car.make, "something")
        self.assertEqual(self.car.model, "X")
        self.assertEqual(self.car.fuel_consumption, 5)
        self.assertEqual(self.car.fuel_capacity, 15)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_property_error(self):
        with self.assertRaises(Exception) as error:
            self.car.make = ""
        self.assertEqual(str(error.exception), "Make cannot be null or empty!")

    def test_model_property_error(self):
        with self.assertRaises(Exception) as error:
            self.car.model = ""
        self.assertEqual(str(error.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_zero(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_consumption = 0
        self.assertEqual(str(error.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_consumption_negative(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_consumption = -1
        self.assertEqual(str(error.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_zero(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_capacity = 0
        self.assertEqual(str(error.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_capacity_negative(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_capacity = -1
        self.assertEqual(str(error.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_negative(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_amount = -1
        self.assertEqual(str(error.exception), "Fuel amount cannot be negative!")

    def test_refuel_zero_error(self):
        with self.assertRaises(Exception) as error:
            self.car.refuel(0)
        self.assertEqual(str(error.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_negative_error(self):
        with self.assertRaises(Exception) as error:
            self.car.refuel(-1)
        self.assertEqual(str(error.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_method_normal(self):
        self.car.fuel_amount = 10
        self.car.refuel(5)
        self.assertEqual(self.car.fuel_amount, 15)

    def test_refuel_method_exceeding(self):
        self.car.fuel_amount = 10
        self.car.refuel(20)
        self.assertEqual(self.car.fuel_amount, 15)

    def test_drive_method_error(self):
        self.car.fuel_amount = 0
        with self.assertRaises(Exception) as error:
            self.car.drive(100)
        self.assertEqual(str(error.exception), "You don't have enough fuel to drive!")

    def test_drive_method(self):
        self.car.fuel_amount = 5
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 0)


if __name__ == '__main__':
    unittest.main()
