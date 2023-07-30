import unittest

from project import Vehicle


class VehicleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(10.5, 190.5)

    def test_default_cons_class_atr(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_initializing(self):
        self.assertEqual(10.5, self.vehicle.fuel)
        self.assertEqual(10.5, self.vehicle.capacity)
        self.assertEqual(190.5, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_driving_with_less_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))
        self.assertEqual(10.5, self.vehicle.fuel)

    def test_driving_with_enough_fuel(self):
        self.vehicle.drive(3)

        self.assertEqual(6.75, self.vehicle.fuel)

    def test_refueling_with_too_much_fuel_raises(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)

        self.assertEqual("Too much fuel", str(ex.exception))
        self.assertEqual(10.5, self.vehicle.fuel)

    def test_correct_refueling(self):
        self.vehicle.capacity = 20

        self.vehicle.refuel(5.5)

        self.assertEqual(16, self.vehicle.fuel)

    def test_the_str_method(self):
        result = self.vehicle.__str__()
        expected = f"The vehicle has 190.5 " \
               f"horse power with 10.5 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()


