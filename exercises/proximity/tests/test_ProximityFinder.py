import unittest

from ProximityFinder import ProximityFinder


class TestProximityFinder(unittest.TestCase):
    def test_simple(self):
        points = [[1, 1], [4, 4], [4, 3], [6, 7]]
        expected = [[4, 4], [4, 3]]
        length, points = ProximityFinder.search(points)
        self.assertEqual(expected, points)

    def test_borders(self):
        points = [[-1, 0], [-1, 7], [5, 0], [5, 7]]
        expected = [[-1, 0], [5, 0]]
        length, points = ProximityFinder.search(points)
        self.assertEqual(expected, points)

    def test_1_dim(self):
        points = [[0], [-15], [5], [7], [-2]]
        expected = [[5], [7]]
        length, points = ProximityFinder.search(points)
        self.assertEqual(expected, points)

    def test_3_dims(self):
        points = [[-1, 0, 8], [-1, 7, -5], [5, 0, 7], [5, 7, 2]]
        expected = [[-1, 0, 8], [5, 0, 7]]
        length, points = ProximityFinder.search(points)
        self.assertEqual(expected, points)

    def test_2_points(self):
        points = [[-1, 0, 8], [-1, 7, -5]]
        expected = [[-1, 0, 8], [-1, 7, -5]]
        length, points = ProximityFinder.search(points)
        self.assertEqual(expected, points)
