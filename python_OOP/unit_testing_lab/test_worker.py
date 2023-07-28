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

import unittest

class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Test", 1000, 50)

    def test_for_correct_initialization(self):
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(50, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_for_low_energy_for_work(self):
        worker = Worker("Test", 1000, 0)
        self.assertEqual(0, worker.energy)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_work_function_properly_working(self):
        self.assertEqual(0, self.worker.money)
        self.assertEqual(50, self.worker.energy)

        self.worker.work()
        expected_money = 1000
        self.assertEqual(expected_money, self.worker.money)
        expected_energy = 50 - 1
        self.assertEqual(expected_energy, self.worker.energy)

        self.worker.work()
        expected_money = 2000
        self.assertEqual(expected_money, self.worker.money)
        expected_energy = 48
        self.assertEqual(expected_energy, self.worker.energy)

    def test_resting(self):
        self.assertEqual(50, self.worker.energy)

        self.worker.rest()
        expected_energy = 50 + 1
        self.assertEqual(expected_energy, self.worker.energy)

    def test_getting_info(self):
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(0, self.worker.money)

        expected_result = f'Test has saved 0 money.'

        self.assertEqual(expected_result, self.worker.get_info())

if __name__ == "__main__":
    unittest.main()



