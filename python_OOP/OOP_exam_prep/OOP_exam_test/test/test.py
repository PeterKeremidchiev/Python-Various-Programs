import unittest

from project.second_hand_car import SecondHandCar


class SecondHandCarTests(unittest.TestCase):
    def setUp(self) -> None:
        self.shc = SecondHandCar("m5", "saloon", 250000, 1000.50)

    def test_initializing(self):
        self.assertEqual("m5", self.shc.model)
        self.assertEqual("saloon", self.shc.car_type)
        self.assertEqual(250000, self.shc.mileage)
        self.assertEqual(1000.50, self.shc.price)
        self.assertEqual([], self.shc.repairs)

    def test_price_setter_with_low_value_raises(self):

        with self.assertRaises(ValueError) as ex:
            self.shc.price = 1.0

        self.assertEqual("Price should be greater than 1.0!", str(ex.exception))

    def test_mileage_setter_with_low_value_raises(self):

        with self.assertRaises(ValueError) as ex:
            self.shc.mileage = 90

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ex.exception))

    def test_promotional_price_with_higher_price(self):

        with self.assertRaises(ValueError) as ex:
            self.shc.set_promotional_price(1100)

        self.assertEqual('You are supposed to decrease the price!', str(ex.exception))
        self.assertEqual(1000.50, self.shc.price)

    def test_promotional_with_lower_price(self):
        result = self.shc.set_promotional_price(900.50)
        exp_res = 'The promotional price has been successfully set.'
        self.assertEqual(exp_res, result)
        self.assertEqual(900.50, self.shc.price)

    def test_need_repair_with_high_price(self):
        result = self.shc.need_repair(600.5, "tyres")
        exp_res = 'Repair is impossible!'
        self.assertEqual(exp_res, result)

    def test_need_repair_with_good_price(self):

        result = self.shc.need_repair(100.5, "tyres")
        exp_res = 'Price has been increased due to repair charges.'

        self.assertEqual(exp_res, result)
        self.assertEqual(1101.0, self.shc.price)
        self.assertEqual(["tyres"], self.shc.repairs)

    def test_gt_mehod_with_different_car_types(self):
        self.other = SecondHandCar("m6", "jeep", 150000, 990.5)

        result = self.shc.__gt__(self.other)
        exp_res = 'Cars cannot be compared. Type mismatch!'
        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test_gt_method_with_same_types(self):
        self.other = SecondHandCar("m6", "saloon", 150000, 990.5)

        result = self.shc.__gt__(self.other)

        self.assertEqual(True, result)

    def test_str_method(self):
        result = self.shc.__str__()
        exp_res = """Model m5 | Type saloon | Milage 250000km
Current price: 1000.50 | Number of Repairs: 0"""
        self.assertEqual(exp_res, result)

