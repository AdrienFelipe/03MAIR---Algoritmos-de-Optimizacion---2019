import unittest

from matrix.Matrix import Matrix


class TestMatrixPower(unittest.TestCase):
    def test_sequential(self):
        a = Matrix(((5, -2), (-4, 5)))
        power = 5
        expected = ((14725, -10378), (-20756, 14725))

        self.assertEqual(expected, a.power_sequential(power).coordinates(), 'Matrix sequential power is incorrect')

    def test_diagonalized(self):
        a = Matrix(((5, -2), (-4, 5)))
        power = 5
        expected = ((14725, -10378), (-20756, 14725))
        result = a.power_diagonalized(power).round(10).coordinates()

        self.assertEqual(expected, result, 'Matrix diagonalized power is incorrect')


if __name__ == '__main__':
    unittest.main()
