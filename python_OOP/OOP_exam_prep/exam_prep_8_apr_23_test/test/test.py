import unittest

from project.tennis_player import TennisPlayer

class TennisPlayerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tennis_player = TennisPlayer("Ivan", 20, 25.5)

    def test_initialization(self):
        self.assertEqual("Ivan", self.tennis_player.name)
        self.assertEqual(20, self.tennis_player.age)
        self.assertEqual(25.5, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_name_setter_with_wrong_value_raises(self):
        with self.assertRaises(ValueError) as va:
            self.tennis_player.name = "pa"

        self.assertEqual("Name should be more than 2 symbols!", str(va.exception))

    def test_age_setter_with_wrong_age_raises(self):
        with self.assertRaises(ValueError) as va:
            self.tennis_player.age = 15
        self.assertEqual("Players must be at least 18 years of age!", str(va.exception))

    def test_adding_new_win_with_already_added_tournament_name(self):
        self.tennis_player.wins = ["Garos"]

        result = self.tennis_player.add_new_win("Garos")
        exp_res = "Garos has been already added to the list of wins!"

        self.assertEqual(exp_res, result)
        self.assertEqual(1, len(self.tennis_player.wins))

    def test_adding_new_win(self):
        result = self.tennis_player.add_new_win("Wimbeldon")

        self.assertEqual(1, len(self.tennis_player.wins))
        self.assertIn("Wimbeldon", self.tennis_player.wins)

    def test_lt_method_with_lower_self_points(self):
        second_player = TennisPlayer("Gosho", 20, 30)
        self.assertEqual(30, second_player.points)
        self.assertEqual(25.5, self.tennis_player.points)

        result = self.tennis_player.__lt__(second_player)
        exp_res = 'Gosho is a top seeded player and he/she is better than Ivan'
        self.assertEqual(exp_res, result)

    def test_lt_method_with_bigger_self_points(self):
        second_player = TennisPlayer("Gosho", 20, 10)
        self.assertEqual(10, second_player.points)
        self.assertEqual(25.5, self.tennis_player.points)

        result = self.tennis_player.__lt__(second_player)
        exp_res = 'Ivan is a better player than Gosho'
        self.assertEqual(exp_res, result)

    def test_str_method(self):
        self.tennis_player.add_new_win("Wimbeldon")
        self.tennis_player.add_new_win("Garos")
        result = self.tennis_player.__str__()
        exp_res = f"Tennis Player: Ivan\n" \
               f"Age: 20\n" \
               f"Points: 25.5\n" \
               f"Tournaments won: Wimbeldon, Garos"

        self.assertEqual(exp_res, result)