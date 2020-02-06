import unittest

from matrix import MatrixException
from matrix.Matrix import Matrix
from matrix.tools.MatrixFactory import MatrixFactory


class TestMatrixFactory(unittest.TestCase):
    def test_coordinates_level_1_not_tuple(self):
        coordinates = 7

        with self.assertRaises(MatrixException.CoordinatesTypeException):
            # noinspection PyTypeChecker
            Matrix(coordinates)

    def test_coordinates_level_2_not_tuple(self):
        coordinates = ((7,), 5)

        with self.assertRaises(MatrixException.CoordinatesTypeException):
            # noinspection PyTypeChecker
            Matrix(coordinates)

    def test_dimensions_not_equal(self):
        coordinates = ((7, 7), (5,))

        with self.assertRaises(MatrixException.DimensionException):
            Matrix(coordinates)

    def test_dimensions(self):
        matrix = Matrix(((1, 2, 3), (4, 5, 6)))
        self.assertEqual(2, matrix.rows_dimension(), 'Incorrect rows dimension count')
        self.assertEqual(3, matrix.columns_dimension(), 'Incorrect columns dimension count')

    def test_immutability(self):
        coordinates = ((1, 2, 3), (4, 5, 6))
        matrix = Matrix(coordinates)
        coordinates += (4,)
        expected = ((1, 2, 3), (4, 5, 6))
        self.assertEqual(expected, matrix.coordinates(), 'Matrix coordinates must be immutable')

    def test_identity_matrix(self):
        matrix = MatrixFactory.identity(4)
        expected = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
        self.assertEqual(expected, matrix.coordinates(), 'Incorrect identity matrix creation')


if __name__ == '__main__':
    unittest.main()
