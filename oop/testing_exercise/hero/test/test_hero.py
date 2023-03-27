import unittest
from project.hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self) -> None:
        self.hero = Hero("TheBest", 1, 100, 10)

    def test_battle_fight_yourself(self):
        enemy = Hero("TheBest", 2, 52, 52)
        with self.assertRaises(Exception) as error:
            self.hero.battle(enemy)
        self.assertEqual(str(error.exception), "You cannot fight yourself")

    def test_battle_hero_low_health(self):
        enemy = Hero("Enemy", 2, 52, 52)
        self.hero.health = 0
        with self.assertRaises(ValueError) as error:
            self.hero.battle(enemy)
        self.assertEqual(str(error.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_draw(self):
        enemy = Hero("Enemy", 1, 10, 10)
        self.hero.health = 10
        result = self.hero.battle(enemy)
        self.assertEqual(result, "Draw")
        self.assertEqual(self.hero.health, 0)
        self.assertEqual(enemy.health, 0)

    def test_battle_hero_win(self):
        enemy = Hero("Enemy", 1, 10, 10)
        result = self.hero.battle(enemy)
        self.assertEqual(result, "You win")
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 95)
        self.assertEqual(self.hero.damage, 15)

    def test_battle_enemy_win(self):
        enemy = Hero("Enemy", 1, 100, 100)
        result = self.hero.battle(enemy)
        self.assertEqual(result, "You lose")
        self.assertEqual(enemy.level, 2)
        self.assertEqual(enemy.health, 95)
        self.assertEqual(enemy.damage, 105)

    def test_str(self):
        expected = f"Hero TheBest: 1 lvl\n" \
                   f"Health: 100\n" \
                   f"Damage: 10\n"
        self.assertEqual(expected, str(self.hero))
