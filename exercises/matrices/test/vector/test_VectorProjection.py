import unittest

from vector.Vector import Vector


class TestVectorProjection(unittest.TestCase):
    def test_projection(self):
        x = Vector((0, 4))
        y = Vector((2, 3))

        # y projection on x
        expected = (0, 3)
        result = y.projection_on(x).coordinates()
        self.assertEqual(expected, result, 'Vector Y projection on X is incorrect')

        # x projection on y
        ratio = (3 * 4) / (2 ** 2 + 3 ** 2)
        expected = (ratio * 2, ratio * 3)
        result = x.projection_on(y).coordinates()
        self.assertEqual(expected, result, 'Vector X projection on Y is incorrect')


if __name__ == '__main__':
    unittest.main()
