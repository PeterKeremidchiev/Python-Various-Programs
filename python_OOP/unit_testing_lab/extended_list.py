class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)

import unittest

class IntegerListTests(unittest.TestCase):
    def setUp(self):
        self.integer = IntegerList(1, 2, 3)

    def test_initialize(self):
        current_len = len(self.integer.get_data())
        self.assertEqual(current_len, len(self.integer.get_data()))
        # self.assertEqual((current_len, len(self.integer._IntegerList.__data)))

    def test_init_not_giving_integers(self):
        integer = IntegerList(4, 5.6, 8)
        self.assertEqual(2, len(integer.get_data()))

    def test_get_data_returns_with_integers(self):
        self.assertEqual([1, 2, 3], self.integer.get_data())

    def test_for_adding_not_integer_element_raises(self):
        self.assertEqual(3, len(self.integer.get_data()))

        for el in [4.5, "assd", {}, False]:
            with self.assertRaises(ValueError) as ex:
                self.integer.add(el)

            self.assertEqual("Element is not Integer", str(ex.exception))

        self.assertEqual(3, len(self.integer.get_data()))

    def test_for_adding_int_element(self):
        self.assertEqual(3, len(self.integer.get_data()))

        self.integer.add(5)
        self.assertEqual(4, len(self.integer.get_data()))
        self.assertIn(5, self.integer.get_data())
        self.assertEqual(self.integer.get_data()[0], 1)
        self.assertEqual(self.integer.get_data()[-1], 5)
        self.assertEqual([1, 2, 3, 5], self.integer.get_data())

    def test_for_romoving_wrong_index_raises(self):
        self.assertEqual(3, len(self.integer.get_data()))

        with self.assertRaises(IndexError) as ex:
            self.integer.remove_index(4)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(3, len(self.integer.get_data()))

    def test_for_removing_the_right_indexes(self):
        self.assertEqual(3, len(self.integer.get_data()))

        expected_element = self.integer.get_data()[1]
        self.assertEqual(2, expected_element)

        self.integer.remove_index(1)
        self.assertEqual(2, len(self.integer.get_data()))
        self.assertNotIn(2, self.integer.get_data())

    def test_getting_index_that_is_not_in_list_raises(self):
        self.assertEqual(3, len(self.integer.get_data()))

        with self.assertRaises(IndexError) as ex:
            self.integer.get(4)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(3, len(self.integer.get_data()))

    def test_get_the_right_index(self):
        self.assertEqual(3, len(self.integer.get_data()))

        self.assertEqual(3, self.integer.get(2))

    def test_inserting_with_wrong_index_raises(self):
        self.assertEqual(3, len(self.integer.get_data()))

        with self.assertRaises(IndexError) as ex:
            self.integer.insert(4, 5)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(3, len(self.integer.get_data()))

    def test_for_inserting_non_int_type_raises(self):
        self.assertEqual(3, len(self.integer.get_data()))

        with self.assertRaises(ValueError) as ex:
            self.integer.insert(2, 5.5)

        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual(3, len(self.integer.get_data()))

    def test_for_correct_inserting(self):
        self.assertEqual(3, len(self.integer.get_data()))
        self.assertEqual([1, 2, 3], self.integer.get_data())
        self.assertEqual([1, 2, 3], self.integer._IntegerList__data)

        self.integer.insert(2, 4)
        self.assertEqual(4, len(self.integer.get_data()))
        self.assertEqual(4, self.integer.get_data()[2])
        self.assertEqual([1, 2, 4, 3], self.integer.get_data())

    def test_for_getting_the_biggest(self):
        self.assertEqual([1, 2, 3], self.integer.get_data())

        sorted_data = sorted(self.integer.get_data(), reverse=True)
        self.assertEqual([3, 2, 1], sorted_data)

        result = self.integer.get_biggest()
        self.assertEqual(3, result)

    def test_getting_index_of_element(self):
        self.assertEqual(3, len(self.integer.get_data()))

        result = self.integer.get_index(1)

        self.assertEqual(0, result)


if __name__ == "__main__":
    unittest.main()





