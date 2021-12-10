import unittest
from one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):
    def test_eq_cities(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = fit_transform(cities)
        expected = [('Moscow', [0, 0, 1]),
         ('New York', [0, 1, 0]),
         ('Moscow', [0, 0, 1]),
         ('London', [1, 0, 0])]
        self.assertEqual(actual, expected)

    def test_not_eq_cities(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = fit_transform(cities)
        expected = [('New York', [0, 0, 1]),
         ('New York', [0, 1, 0]),
         ('Moscow', [0, 0, 1]),
         ('London', [1, 0, 0])]

        self.assertNotEqual(actual, expected)

    def test_not_in_cities(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = fit_transform(cities)
        self.assertNotIn('Ryazan', actual)

    def test_in_cities(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = fit_transform(cities)
        self.assertIn(('Moscow', [0, 0, 1]), actual)

    def test_exception(self):
        self.assertRaises(TypeError, fit_transform, 123)


if __name__ == '__main__':
   unittest.main()
