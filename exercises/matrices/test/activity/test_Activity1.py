import unittest

from vector.Vector import Vector
from requirements.areorthogonal import areorthogonal
from requirements.vecdot import vecdot


class TestActivity1(unittest.TestCase):

    # Exercise 1.a
    def test_vecdot(self):
        x = Vector((4, 5, 1))
        y = Vector((2, 2, 8))

        self.assertEqual(26, vecdot(x, y), 'Vector product returned an invalid value')

    # Exercise 1.b
    def test_areorthogonal(self):
        x = Vector((-6, 3))
        y = Vector((1, 2))

        self.assertTrue(areorthogonal(x, y), 'Vectors x and y are not orthogonal.')


if __name__ == '__main__':
    unittest.main()
