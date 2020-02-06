import unittest

from requirements import vecnorm
from vector.Vector import Vector


class TestActivity2(unittest.TestCase):

    # Exercise 2.a: Infinite norm or max norm
    def test_max_norm(self):
        v = Vector((1.3, 2.2, 3.1))
        self.assertEqual(3.1, vecnorm.max_norm(v), 'Infinite norm is incorrect.')

    # Exercise 2.a: Taxicab or Manhattan norm
    def test_taxicab_norm(self):
        v = Vector((1.3, 2.2, 3.1))
        self.assertEqual(6.6, vecnorm.taxicab_norm(v), 'Taxicab norm is incorrect.')

    # Exercise 2.a: Euclidean norm
    def test_euclidean_norm(self):
        v = Vector((13, 56))
        expected = (v.coordinates()[0] ** 2 + v.coordinates()[1] ** 2) ** (1 / 2)
        self.assertEqual(expected, vecnorm.euclidean_norm(v), 'Euclidean norm is incorrect.')

    # Exercise 2.b: Projection and orthogonal
    def test_projection_orthogonal(self):
        u = Vector.random(3)
        v = Vector.random(3)
        p = u.projection_on(v)
        o = u.orthogonal_on(v)

        self.assertEqual(0., round(p.product(o), 6), 'Product p·o should be null')


if __name__ == '__main__':
    unittest.main()
