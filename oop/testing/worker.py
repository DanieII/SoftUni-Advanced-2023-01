import unittest


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(unittest.TestCase):

    def setUp(self) -> None:
        self.worker = Worker("Ivan", 3000, 10)

    def test_for_correct_initialization(self):
        self.assertEqual(self.worker.name, "Ivan")
        self.assertEqual(self.worker.salary, 3000)
        self.assertEqual(self.worker.energy, 10)

    def test_if_the_energy_is_incremented_after_resting(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 11)

    def test_for_error_after_working_with_negative_energy(self):
        self.worker.energy = -1
        with self.assertRaises(Exception) as error:
            self.worker.work()
        self.assertEqual(str(error.exception), 'Not enough energy.')

    def test_for_error_after_working_with_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as error:
            self.worker.work()
        self.assertEqual(str(error.exception), 'Not enough energy.')

    def test_if_money_increases_after_working(self):
        expected_money = self.worker.money + self.worker.salary
        self.worker.work()
        self.assertEqual(self.worker.money, expected_money)

    def test_if_energy_decreases_after_working(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 9)

    def test_if_the_get_info_method_returns_the_correct_string(self):
        expected_string = f'{self.worker.name} has saved {self.worker.money} money.'
        self.assertEqual(self.worker.get_info(), expected_string)


if __name__ == '__main__':
    unittest.main()
