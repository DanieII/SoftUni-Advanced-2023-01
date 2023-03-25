import unittest


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


class IntegerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.list = IntegerList(1, 2, 3, 4.5, "string")

    def test_constructor_for_other_than_integers(self):
        result = self.list.get_data()
        expected = [1, 2, 3]
        self.assertEqual(result, expected)

    def test_add_method(self):
        result = self.list.add(5)
        expected = [1, 2, 3, 5]
        self.assertEqual(result, expected)

    def test_add_method_error(self):
        with self.assertRaises(ValueError) as error:
            self.list.add("not an integer")
        self.assertEqual(str(error.exception), "Element is not Integer")

    def test_remove_index_method(self):
        result = self.list.remove_index(2)
        expected = 3
        self.assertEqual(result, expected)

    def test_remove_index_method_error(self):
        with self.assertRaises(IndexError) as error:
            self.list.remove_index(3)
        self.assertEqual(str(error.exception), "Index is out of range")

    def test_get_method(self):
        result = self.list.get(2)
        expected = 3
        self.assertEqual(result, expected)

    def test_get_method_error(self):
        with self.assertRaises(IndexError) as error:
            self.list.get(3)
        self.assertEqual(str(error.exception), "Index is out of range")

    def test_insert_method(self):
        self.list.insert(2, 5)
        result = self.list.get_data()
        expected = [1, 2, 5, 3]
        self.assertEqual(result, expected)

    def test_insert_method_errors(self):
        with self.assertRaises(IndexError) as index:
            self.list.insert(3, 1)
        with self.assertRaises(ValueError) as value:
            self.list.insert(1, "not an index")
        self.assertEqual(str(index.exception), "Index is out of range")
        self.assertEqual(str(value.exception), "Element is not Integer")

    def test_get_biggest_method(self):
        result = self.list.get_biggest()
        expected = 3
        self.assertEqual(result, expected)

    def test_get_index_method(self):
        result = self.list.get_index(3)
        expected = 2
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
