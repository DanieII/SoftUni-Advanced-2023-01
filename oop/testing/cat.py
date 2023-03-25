import unittest


class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


class CatTests(unittest.TestCase):

    def setUp(self) -> None:
        self.cat = Cat("Koki")

    def test_if_cat_size_increases_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_if_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_for_error_when_feeding_an_already_fed_cat(self):
        self.cat.eat()
        with self.assertRaises(Exception) as error:
            self.cat.eat()
        self.assertEqual(str(error.exception), 'Already fed.')

    def test_for_error_if_a_not_fed_cat_sleeps(self):
        with self.assertRaises(Exception) as error:
            self.cat.sleep()
        self.assertEqual(str(error.exception), 'Cannot sleep while hungry')

    def test_if_cat_is_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
