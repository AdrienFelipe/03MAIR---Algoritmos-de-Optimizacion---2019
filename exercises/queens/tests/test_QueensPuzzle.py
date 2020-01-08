import unittest

from QueensPuzzle import QueensPuzzle


class TestQueensPuzzle(unittest.TestCase):

    def test_board_size_4(self):
        solutions = QueensPuzzle.solve(4)
        expected = [(1, 3, 0, 2), (2, 0, 3, 1)]
        self.assertEqual(expected, solutions)

    def test_board_size_5(self):
        solutions = QueensPuzzle.solve(5)
        expected = [
            (0, 2, 4, 1, 3), (0, 3, 1, 4, 2), (1, 3, 0, 2, 4), (1, 4, 2, 0, 3), (2, 0, 3, 1, 4),
            (2, 4, 1, 3, 0), (3, 0, 2, 4, 1), (3, 1, 4, 2, 0), (4, 1, 3, 0, 2), (4, 2, 0, 3, 1),
        ]
        self.assertEqual(expected, solutions)
