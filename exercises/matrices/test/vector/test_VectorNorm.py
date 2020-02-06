import unittest

from vector.Vector import Vector


class TestVectorNorm(unittest.TestCase):

    def test_infinite_norm(self):
        x = Vector((1, 2, 3))
        self.assertEqual(3, x.norm(-1), 'Infinite norm is incorrect')

    def test_zero_norm(self):
        x = Vector((1, 2, 3))
        self.assertEqual(0, x.norm(0), 'Zero norm is incorrect')

    def test_taxicab_norm(self):
        x = Vector((1.5, 2.5, 3))
        self.assertEqual(7, x.norm(1), 'Taxicab norm is incorrect')

    def test_euclidean_norm(self):
        x = Vector((1, 2, 3))
        expected = (1 + 4 + 9) ** (1 / 2)
        self.assertEqual(expected, x.norm(2), 'Euclidean norm is incorrect')

    def test_p_norm_5(self):
        x = Vector((1, 2, 3))
        expected = (1 ** 5 + 2 ** 5 + 3 ** 5) ** (1 / 5)
        self.assertEqual(expected, x.norm(5), 'P norm of 5 is incorrect')

    def test_p_norm_10_dim_1(self):
        x = Vector((347,))
        p = 10
        expected = (x.coordinates()[0] ** p) ** (1 / p)
        self.assertEqual(expected, x.norm(p), 'P norm of 10 with dimension 1 is incorrect')


if __name__ == '__main__':
    unittest.main()
