import unittest

from matrix import MatrixException
from matrix.Matrix import Matrix


class TestMatrixDeterminant(unittest.TestCase):
    def test_sub_matrix(self):
        matrix = Matrix(((1, 2, 3), (2, 3, 5), (4, 2, 1)))
        result = matrix.sub_matrix(0, 1)
        expected = ((2, 5), (4, 1))
        self.assertEqual(expected, result.coordinates(), 'Determinant sub matrix is incorrect')

    def test_determinant(self):
        matrix = Matrix(((-2, 2, -3), (-1, 1, 3), (2, 0, -1)))
        self.assertEqual(18, matrix.determinant(), 'Determinant 1 calculation is incorrect')

        matrix = Matrix(((4, 7), (6, 2)))
        self.assertEqual(-34, matrix.determinant(), 'Determinant 2 calculation is incorrect')

        matrix = Matrix(((4,),))
        self.assertEqual(4, matrix.determinant(), 'Determinant 3 calculation is incorrect')

        matrix = Matrix(((1, 7, 5, 4), (3, 2, 4, 5), (6, 7, 8, 5), (4, 8, 9, 3)))
        self.assertEqual(-253, matrix.determinant(), 'Determinant 4 calculation is incorrect')

    def test_square_exception(self):
        matrix = Matrix(((1, 2, 3), (2, 3, 5)))
        with self.assertRaises(MatrixException.NotSquareException):
            matrix.determinant()


if __name__ == '__main__':
    unittest.main()
