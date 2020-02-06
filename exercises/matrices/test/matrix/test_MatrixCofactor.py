import unittest

from matrix.Matrix import Matrix


class TestMatrixCofactor(unittest.TestCase):
    def test_cofactor(self):
        matrix = Matrix(((1, 0, 5), (2, 1, 6), (3, 4, 0)))
        expected = ((-24, 18, 5), (20, -15, -4), (-5, 4, 1))
        self.assertEqual(expected, matrix.cofactor().coordinates(), 'Matrix inverse is incorrect')


if __name__ == '__main__':
    unittest.main()
