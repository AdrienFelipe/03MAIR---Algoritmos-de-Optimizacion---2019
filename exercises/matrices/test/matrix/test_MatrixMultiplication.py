import unittest

from matrix.Matrix import Matrix


class TestMatrixMultiplication(unittest.TestCase):
    def test_scalar_multiplication(self):
        matrix = Matrix(((1, 2, 3), (4, 5, 6)))
        expectation = ((2, 4, 6), (8, 10, 12))
        self.assertEqual(expectation, matrix.multiply(2).coordinates(), 'Matrix multiplication is incorrect')


if __name__ == '__main__':
    unittest.main()
