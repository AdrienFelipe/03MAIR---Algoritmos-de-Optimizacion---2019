import unittest

from matrix.Matrix import Matrix
from matrix import MatrixException


class TestMatrixInverse(unittest.TestCase):
    def test_inverse(self):
        matrix = Matrix(((0, -3, -2), (1, -4, -2), (-3, 4, 1)))
        expected = ((4, -5, -2), (5, -6, - 2), (-8, 9, 3))
        self.assertEqual(expected, matrix.inverse().coordinates(), 'Matrix inverse is incorrect')

    def test_null_determinant_error(self):
        matrix = Matrix(((1, 4), (1, 4)))
        with self.assertRaises(MatrixException.NullDeterminantException):
            matrix.inverse()


if __name__ == '__main__':
    unittest.main()
