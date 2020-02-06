import unittest

from matrix.Matrix import Matrix
from matrix import MatrixException


class TestMatrixProduct(unittest.TestCase):

    def test_dimension_error_2x3_2x3(self):
        a = Matrix(((1, 2, 1), (3, 2, 0)))  # 2x3
        b = Matrix(((6, 0, 3), (0, 8, 1)))  # 2x3

        with self.assertRaises(MatrixException.DimensionException):
            a.product(b)

    def test_dimension_error_2x2_3x2(self):
        a = Matrix(((1, 2), (3, 2)))  # 2x2
        b = Matrix(((6, 0), (8, 1), (2, 7)))  # 3x2

        with self.assertRaises(MatrixException.DimensionException):
            a.product(b)

    def test_product(self):
        a = Matrix(((6, 0, 3), (0, 8, 1)))  # 2x3
        b = Matrix(((1, 2), (3, 2), (4, 6)))  # 3x2
        expected = ((6 + 3 * 4, 6 * 2 + 3 * 6), (8 * 3 + 4, 8 * 2 + 6))

        self.assertEqual(expected, a.product(b).coordinates(), 'Incorrect matrix product')


if __name__ == '__main__':
    unittest.main()
