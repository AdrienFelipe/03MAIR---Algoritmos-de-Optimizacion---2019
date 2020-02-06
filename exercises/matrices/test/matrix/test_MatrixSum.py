import unittest

from matrix.Matrix import Matrix
from matrix import MatrixException


class TestMatrixSum(unittest.TestCase):

    def test_dimension_error(self):
        a = Matrix(((1, 2), (3, 4)))
        b = Matrix(((1, 2, 3), (3, 4, 5)))

        with self.assertRaises(MatrixException.DimensionException):
            a.add(b)

    def test_add(self):
        a = Matrix(((1, 2), (3, 4)))
        b = Matrix(((4, 5), (4, 5)))
        expected = ((5, 7), (7, 9))

        self.assertEqual(expected, a.add(b).coordinates(), 'Matrix addition is incorrect')

    def test_subtract(self):
        a = Matrix(((1, 2), (3, 4)))
        b = Matrix(((4, 5), (4, 5)))
        expected = ((-3, -3), (-1, -1))

        self.assertEqual(expected, a.subtract(b).coordinates(), 'Matrix subtraction is incorrect')


if __name__ == '__main__':
    unittest.main()
