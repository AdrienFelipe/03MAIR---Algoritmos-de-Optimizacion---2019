import numpy

from vector import Vector


class VectorFactory:

    @staticmethod
    def random(dimension: int) -> Vector:
        coordinates = ()
        for key in range(dimension):
            # Populate a random float value in [-100, 100]
            # limited to only two decimals.
            value = round(numpy.random.rand() * 200 - 100, 2)
            coordinates += (value,)

        return Vector.Vector(coordinates)
