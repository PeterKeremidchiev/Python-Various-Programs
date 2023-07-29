class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


import unittest

class CarManagerTests(unittest.TestCase):
    def setUp(self):
        self.car = Car("Skoda", "Fabia", 6, 50)

    def test_initializing(self):

        self.assertEqual("Skoda", self.car.make)
        self.assertEqual("Fabia", self.car.model)
        self.assertEqual(6, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_setter_for_make_with_no_value_raises(self):

        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_setter_for_model_with_no_value_raises(self):

        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_setter_for_fuel_cons_with_zero_raises(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_setter_for_fuel_capacity_with_zero_raises(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_for_negative_fuel_amount_raises(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_for_zero_refueling_raises(self):

        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_for_refueling(self):

        self.assertEqual(0, self.car.fuel_amount)

        self.car.refuel(60)

        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(50, self.car.fuel_amount)

    def test_for_less_than_needed_fuel_amount_raises(self):
        self.car.fuel_amount = 30

        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

        self.assertEqual(30, self.car.fuel_amount)

    def test_for_enough_fuel_amount_for_driving(self):

        self.car.fuel_amount = 50

        self.car.drive(100)
        expected_fuel_amount = 50 - 6
        self.assertEqual(expected_fuel_amount, self.car.fuel_amount)


if __name__ == "__main__":
    unittest.main()

