import unittest

from project import Mammal


class MammalTests(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Test", "dog", "waf")

    def test_initializing(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("dog", self.mammal.type)
        self.assertEqual("waf", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_the_sound(self):
        expected_result = f"Test makes waf"

        self.assertEqual(expected_result, self.mammal.make_sound())

    def test_getting_the_kingdom(self):
        expected_result = "animals"

        self.assertEqual(expected_result, self.mammal.get_kingdom())

    def test_info_method(self):
        expected_result = "Test is of type dog"

        self.assertEqual(expected_result, self.mammal.info())


if __name__ == "__main__":
    unittest.main()
