import unittest

from matrix.Matrix import Matrix


class TestMatrixTranspose(unittest.TestCase):
    def test_matrix_transpose(self):
        matrix = Matrix(((1, 5, 7), (8, 3, -1), (0, -7, 8)))
        expected = ((1, 8, 0), (5, 3, -7), (7, -1, 8))
        self.assertEqual(expected, matrix.transpose().coordinates())

        matrix = Matrix(((1, 5), (8, 3), (0, -7)))
        expected = ((1, 8, 0), (5, 3, -7))
        self.assertEqual(expected, matrix.transpose().coordinates())

        matrix = Matrix(((1, 5, 7), (8, 3, -1)))
        expected = ((1, 8), (5, 3), (7, -1))
        self.assertEqual(expected, matrix.transpose().coordinates())


if __name__ == '__main__':
    unittest.main()
