import unittest

from project import Hero


class HeroTests(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Zoro", 5, 99.5, 70.5)

    def test_initializing(self):
        self.assertEqual("Zoro", self.hero.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(99.5, self.hero.health)
        self.assertEqual(70.5, self.hero.damage)

    def test_battle_with_the_same_username_raises(self):
        enemy_hero = Hero("Zoro", 50, 99.5, 70.5)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_low_health_raises(self):
        enemy_hero = Hero("Pesho", 50, 99.5, 70.5)
        self.hero.health = 0

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_with_enemy_low_health_raises(self):
        enemy_hero = Hero("Pesho", 50, 0, 70.5)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual("You cannot fight Pesho. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        enemy_hero = Hero("Pesho", 5, 99.5, 50.5)

        result = self.hero.battle(enemy_hero)

        self.assertEqual(-153, self.hero.health)
        self.assertEqual(-253, enemy_hero.health)
        self.assertEqual("Draw", result)

    def test_battle_you_win(self):
        enemy_hero = Hero("Pesho", 5, 20.5, 2.5)
        self.hero = Hero("Zoro", 5, 99.5, 5.5)

        result = self.hero.battle(enemy_hero)
        self.assertEqual(92, self.hero.health)
        self.assertEqual(-7, enemy_hero.health)
        self.assertEqual("You win", result)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(10.5, self.hero.damage)

    def test_battle_you_lose(self):
        enemy_hero = Hero("Pesho", 5, 40, 3)
        self.hero = Hero("Zoro", 5, 10, 5)

        result = self.hero.battle(enemy_hero)
        self.assertEqual(-5, self.hero.health)
        self.assertEqual(20, enemy_hero.health)
        self.assertEqual("You lose", result)
        self.assertEqual(6, enemy_hero.level)
        self.assertEqual(8, enemy_hero.damage)

    def test_the_str_method(self):
        result = self.hero.__str__()
        expected = f"Hero Zoro: 5 lvl\n" \
               f"Health: 99.5\n" \
               f"Damage: 70.5\n"

        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()







