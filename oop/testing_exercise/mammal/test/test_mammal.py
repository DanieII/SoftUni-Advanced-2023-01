import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal("Sancho", "elephant", "wuuu")

    def test_constructor(self):
        self.assertEqual(self.mammal.name, "Sancho")
        self.assertEqual(self.mammal.type, "elephant")
        self.assertEqual(self.mammal.sound, "wuuu")
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), "Sancho makes wuuu")

    def test_info(self):
        self.assertEqual(self.mammal.info(), "Sancho is of type elephant")
