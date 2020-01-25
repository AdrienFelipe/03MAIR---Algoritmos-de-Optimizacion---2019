import unittest

import BranchPound


class TestBranchPound(unittest.TestCase):
    def setUp(self):
        self.costs = (
            # Actor0, actor1, actor2
            [1, 0, 1],  # Take0
            [0, 0, 1],  # Take1
            [0, 0, 1],  # Take2
            [1, 1, 0],  # Take3
        )
        self.max_takes = 2

    def test_calculate_solution_cost(self):
        solution = (0, 3, 1, 2)
        result = BranchPound.calculate_cost(solution, 2, self.costs)

        self.assertEqual(4, result)

    def test_calculate_partial_solution_cost(self):
        solution = (0, 3, 1)
        result = BranchPound.calculate_cost(solution, 2, self.costs)

        self.assertEqual(4, result)

    def test_calculate_empty_solution_cost(self):
        solution = ()
        result = BranchPound.calculate_cost(solution, 2, self.costs)

        self.assertEqual(0, result)

    def test_get_next_solutions_full(self):
        solution = (0, 3, 1,)
        expected = [(0, 3, 1, 2)]
        results = BranchPound.create_child_solutions(solution, self.costs, self.max_takes)

        self.assertEqual(expected, results)

    def test_get_next_solutions_partial(self):
        solution = (0,)
        expected = [(0, 1), (0, 2), (0, 3)]
        results = BranchPound.create_child_solutions(solution, self.costs, self.max_takes)

        self.assertEqual(expected, results)

    def test_get_next_solutions_empty(self):
        solution = ()
        expected = [(0,), (1,), (2,), (3,)]
        results = BranchPound.create_child_solutions(solution, self.costs, self.max_takes)

        self.assertEqual(expected, results)

    def test_estimate_lowest_cost(self):
        solution = (3,)
        expected = 3
        result = BranchPound.estimate_lowest_cost(solution, 2, self.costs)

        self.assertEqual(expected, result)

    def test_simple(self):
        expected = (0, 3, 1, 2)
        result = BranchPound.branch_and_pound(self.costs, 2)
        self.assertEqual(expected, result)

    def test_full(self):
        costs = (
            [0, 1, 0, 1], [1, 1, 0, 0], [0, 1, 0, 0],
            [0, 1, 1, 0], [1, 0, 0, 0], [0, 0, 1, 0],
            [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0],
        )
        expected = (0, 2, 6, 3, 5, 1, 4, 7, 8)
        result = BranchPound.branch_and_pound(costs, 3)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
