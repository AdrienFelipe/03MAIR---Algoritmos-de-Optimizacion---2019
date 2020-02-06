import unittest
from vector.Vector import Vector
from vector.VectorException import VectorDimensionException


class TestVectorProduct(unittest.TestCase):
    def test_vector_product_dim_1(self):
        x = Vector((7,))
        y = Vector((3,))

        self.assertEqual(21, x.product(y), 'Vector product is incorrect')

    def test_vector_product_dim_n(self):
        x = Vector((1, 2, 3, 4))
        y = Vector((6, 5, 4, 3))
        expected = 1 * 6 + 2 * 5 + 3 * 4 + 4 * 3

        self.assertEqual(expected, x.product(y), 'Vector product is incorrect')

    def test_vector_product_dim_error(self):
        x = Vector((1, 2))
        y = Vector((6, 5, 4, 3))

        with self.assertRaises(VectorDimensionException):
            x.product(y)


if __name__ == '__main__':
    unittest.main()
