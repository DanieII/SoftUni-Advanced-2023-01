import unittest
from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(50, 200)

    def test_constructor(self):
        self.assertEqual(self.vehicle.fuel, 50)
        self.assertEqual(self.vehicle.capacity, 50)
        self.assertEqual(self.vehicle.horse_power, 200)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)

    def test_drive_error(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.drive(100)
        self.assertEqual(str(error.exception), "Not enough fuel")

    def test_drive_success(self):
        self.vehicle.drive(4)
        self.assertEqual(self.vehicle.fuel, 45)

    def test_refuel_error(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.refuel(1)
        self.assertEqual(str(error.exception), "Too much fuel")

    def test_refuel_success(self):
        self.vehicle.fuel = 1
        self.vehicle.refuel(1)
        self.assertEqual(self.vehicle.fuel, 2)

    def test_str(self):
        expected = f"The vehicle has 200 " \
                 f"horse power with 50 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, str(self.vehicle))


if __name__ == '__main__':
    unittest.main()
