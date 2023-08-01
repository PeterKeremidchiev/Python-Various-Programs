import unittest

from project.movie import Movie


class MovieTests(unittest.TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Test", 2000, 9.5)

    def test_initializing(self):
        self.assertEqual("Test", self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(9.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_the_name_setter_with_no_value_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_the_year_setter_with_not_valid_year_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1885

        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_adding_actor_that_is_not_in_the_list(self):
        self.assertEqual([], self.movie.actors)

        self.movie.add_actor("Gosho")
        self.assertEqual(["Gosho"], self.movie.actors)
        self.assertEqual(1, len(self.movie.actors))
        self.assertIn("Gosho", self.movie.actors)

    def test_adding_actor_that_is_already_in_the_list(self):
        self.movie.actors = ["Pesho"]

        result = self.movie.add_actor("Pesho")
        self.assertEqual(f"Pesho is already added in the list of actors!", result)
        self.assertEqual(1, len(self.movie.actors))
        self.assertIn("Pesho", self.movie.actors)

    def test_gt_with_better_self_rating(self):
        other_movie = Movie("Test2", 2000, 7.5)

        result = self.movie.__gt__(other_movie)

        self.assertEqual('"Test" is better than "Test2"', result)
        self.assertEqual(7.5, other_movie.rating)
        self.assertEqual(9.5, self.movie.rating)

    def test_gt_with_better_rating_on_second_film(self):
        other_movie = Movie("Test2", 2000, 10)

        result = self.movie.__gt__(other_movie)

        self.assertEqual('"Test2" is better than "Test"', result)
        self.assertEqual(10, other_movie.rating)
        self.assertEqual(9.5, self.movie.rating)

    def test_the_repr_method(self):
        self.movie.actors = ["gosho", "pesho"]

        result = self.movie.__repr__()
        self.assertEqual(f"Name: Test\n"
                         f"Year of Release: 2000\n"
                         f"Rating: 9.50\n"
                         f"Cast: gosho, pesho", result)

if __name__ == "__main__":
    unittest.main()
