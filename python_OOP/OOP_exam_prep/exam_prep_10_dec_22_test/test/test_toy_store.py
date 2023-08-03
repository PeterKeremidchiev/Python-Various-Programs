import unittest

from project.toy_store import ToyStore

class ToyStoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.toystore = ToyStore()

    def test_initializing(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toystore.toy_shelf)

    def test_adding_toy_on_non_existing_shelv_raises(self):

        with self.assertRaises(Exception) as ex:
            self.toystore.add_toy("Z", "test")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_adding_toy_that_is_on_shelf_raises(self):
        self.toystore.toy_shelf["A"] = "test_toy"

        with self.assertRaises(Exception) as ex:
            self.toystore.add_toy("A", "test_toy")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_adding_toy_on_taken_shelf_raises(self):
        self.toystore.toy_shelf["A"] = "test_toy"

        with self.assertRaises(Exception) as ex:
            self.toystore.add_toy("A", "toy")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_adding_toy_happy_scenario(self):
        result = self.toystore.add_toy("A", "toy")
        expected_return = "Toy:toy placed successfully!"

        self.assertEqual(expected_return, result)
        self.assertEqual({
            "A": "toy",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toystore.toy_shelf)

    def test_removing_toy_from_non_existing_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toystore.remove_toy("Z", "test")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_removing_toy_with_non_existing_name_raises(self):
        self.toystore.toy_shelf["A"] = "test_toy"

        with self.assertRaises(Exception) as ex:
            self.toystore.remove_toy("A", "test")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_removing_happy_scenario(self):
        self.toystore.toy_shelf["A"] = "test_toy"

        result = self.toystore.remove_toy("A", "test_toy")
        expected_return = "Remove toy:test_toy successfully!"

        self.assertEqual(expected_return, result)
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toystore.toy_shelf)