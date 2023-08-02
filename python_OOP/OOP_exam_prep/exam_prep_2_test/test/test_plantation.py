import unittest

from project import Plantation

class PlantationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(10)

    def test_initialization(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_the_size_setter_with_negative_raises(self):

        with self.assertRaises(ValueError) as ex:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_hiring_worker_that_already_works_raises(self):
        self.plantation.workers = ["Pesho", "Gosho"]

        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker("Gosho")

        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_hiring_worker_with_new_worker(self):
        self.plantation.workers = ["Pesho", "Gosho"]

        result = self.plantation.hire_worker("Ivan")
        self.assertEqual(["Pesho", "Gosho", "Ivan"], self.plantation.workers)
        self.assertEqual("Ivan successfully hired.", result)
        self.assertEqual(3, len(self.plantation.workers))

    def test_len_method(self):
        self.plantation.plants = {"Gosho": ["tomato", "pepper"], "Pesho": ["potato"]}

        result = self.plantation.__len__()
        self.assertEqual(3, result)

    def test_planting_with_wrong_worker_raises(self):

        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Ivan", "tomato")

        self.assertEqual("Worker with name Ivan is not hired!", str(ex.exception))

    def test_for_full_plantation_raises(self):
        self.plantation.size = 0
        self.plantation.hire_worker("Test")

        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Test", "rose")

        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_if_worker_is_hired(self):
        self.plantation.workers = ["Gosho", "Pesho"]
        self.plantation.plants = {"Gosho": [], "Pesho": []}

        result = self.plantation.planting("Gosho", "rose")
        self.assertEqual("Gosho planted rose.", result)
        self.assertEqual({"Gosho": ["rose"], "Pesho": []}, self.plantation.plants)

        result = self.plantation.planting("Gosho", "tomato")
        self.assertEqual("Gosho planted tomato.", result)
        self.assertEqual({"Gosho": ["rose", "tomato"], "Pesho": []}, self.plantation.plants)


    def test_planting_with_non_existing_worker(self):
        self.plantation.workers = ["Gosho", "Pesho"]

        result = self.plantation.planting("Gosho", "rose")

        self.assertEqual({"Gosho": ["rose"]}, self.plantation.plants)
        self.assertEqual("Gosho planted it's first rose.", result)

    def test_str_method(self):
        self.plantation.workers = ["Pesho", "Gosho"]
        self.plantation.plants = {"Gosho": ["tomato", "pepper"], "Pesho": ["potato"]}

        result = self.plantation.__str__()
        expected_res = "Plantation size: 10\n" + "Pesho, Gosho\n" + "Gosho planted: tomato, pepper\n" + "Pesho planted: potato"

        self.assertEqual(expected_res, result)

    def test_repr_method(self):
        self.plantation.workers = ["Pesho", "Gosho"]

        result = self.plantation.__repr__()
        expected_res = 'Size: 10\n' + 'Workers: Pesho, Gosho'

        self.assertEqual(expected_res, result)

if __name__ == "__main__":
    unittest.main()





