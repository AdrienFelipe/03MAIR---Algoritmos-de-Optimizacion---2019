import unittest

from vector.Vector import Vector


class TestVectorMultiplication(unittest.TestCase):
    def test_scalar_multiplication(self):
        x = Vector((3, 5, 7))
        result = x.scalar_multiplication(3).coordinates()
        expected = (9, 15, 21)
        self.assertEqual(expected, result, 'Vector scalar multiplication is incorrect')


if __name__ == '__main__':
    unittest.main()
