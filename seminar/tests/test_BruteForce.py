import unittest

import BruteForce


class TestBruteForce(unittest.TestCase):
    def setUp(self):
        self.costs = (
            [1, 0, 1],
            [0, 0, 1],
            [0, 0, 1],
            [1, 1, 0],
        )
        self.max_takes = 2

    def test_get_next_solutions_full(self):
        solution = (0, 3, 2)
        expected = [(0, 3, 2, 1)]
        results = BruteForce.next_level(self.costs, solution)

        self.assertEqual(expected, results)

    def test_get_next_solutions_partial(self):
        solution = (3, 1)
        expected = [(3, 1, 0, 2), (3, 1, 2, 0)]
        results = BruteForce.next_level(self.costs, solution)

        self.assertEqual(expected, results)

    def test_get_next_solutions_empty(self):
        costs = ((0, 1), (1, 0), (1, 1))
        expected = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
        results = BruteForce.next_level(costs)

        self.assertEqual(expected, results)

    def test_simple(self):
        expected = (0, 3, 1, 2)
        result = BruteForce.brute_force(self.costs, 2)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
