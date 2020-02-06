import unittest

from vector.Vector import Vector


class TestVectorSum(unittest.TestCase):
    def test_add(self):
        x = Vector((3, 6))
        y = Vector((2, 4))

        self.assertEqual((5, 10), x.add(y).coordinates(), 'Vector addition is incorrect')

    def test_subtract(self):
        x = Vector((3, 6))
        y = Vector((2, 4))

        self.assertEqual((1, 2), x.subtract(y).coordinates(), 'Vector subtraction is incorrect')


if __name__ == '__main__':
    unittest.main()
