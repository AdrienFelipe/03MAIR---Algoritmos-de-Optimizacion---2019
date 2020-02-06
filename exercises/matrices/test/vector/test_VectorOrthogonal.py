import unittest

from vector.Vector import Vector


class TestVectorOrthogonal(unittest.TestCase):
    def test_orthogonal(self):
        x = Vector((0, 4))
        y = Vector((2, 3))

        # y orthogonal on x
        expected = (2, 0)
        result = y.orthogonal_on(x).coordinates()
        self.assertEqual(expected, result, 'Vector Y orthogonal on X is incorrect')

        # x orthogonal on y
        x_y_product_ratio = (3 * 4) / (2 ** 2 + 3 ** 2)
        expected = (0 - x_y_product_ratio * 2, 4 - x_y_product_ratio * 3)
        result = x.orthogonal_on(y).coordinates()
        self.assertEqual(expected, result, 'Vector X orthogonal on Y is incorrect')


if __name__ == '__main__':
    unittest.main()
