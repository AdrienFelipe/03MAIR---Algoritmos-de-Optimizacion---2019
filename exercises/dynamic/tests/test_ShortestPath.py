import unittest

from ShortestPath import ShortestPath


class ShortestPathTest(unittest.TestCase):

    def setUp(self):
        self.prices = [
            [0, 5, 4, 3, None, None, None],
            [None, 0, None, 2, 3, None, 11],
            [None, None, 0, 1, None, 4, 10],
            [None, None, None, 0, 5, 6, 9],
            [None, None, None, None, 0, None, 4],
            [None, None, None, None, None, 0, 3],
            [None, None, None, None, None, None, 0]
        ]

    def test_river_full_path(self):
        result = ShortestPath.calculate(self.prices, 0, 6)
        expected = [0, 2, 5, 6]

        self.assertEqual(expected, result)

    def test_river_partial_start_path(self):
        result = ShortestPath.calculate(self.prices, 1, 6)
        expected = [1, 4, 6]

        self.assertEqual(expected, result)

    def test_river_partial_end_path(self):
        result = ShortestPath.calculate(self.prices, 0, 5)
        expected = [0, 2, 5]

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
