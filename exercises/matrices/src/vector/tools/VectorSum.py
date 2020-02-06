from vector import Vector
from vector.VectorException import VectorDimensionException


class VectorSum:

    @staticmethod
    def add(x: Vector, y: Vector) -> Vector:
        """ Add vector Y to vector X"""
        # Make sure a vector product can be calculated.
        VectorSum.__validate(x, y)

        coordinates = ()
        for key, x_value in enumerate(x.coordinates()):
            y_value = y.coordinates()[key]
            coordinates += (x_value + y_value,)

        return Vector.Vector(coordinates)

    @staticmethod
    def subtract(x: Vector, y: Vector) -> Vector:
        return x.add(y.scalar_multiplication(-1))

    @staticmethod
    def __validate(x: Vector, y: Vector) -> None:
        # Vectors must have the same dimensions to be added together.
        if not x.dimension() == y.dimension():
            raise VectorDimensionException('Vectors must have the same dimension.')
