from vector import Vector


class VectorMultiplication:

    @staticmethod
    def calculate(vector: Vector, scalar: float) -> Vector:
        coordinates = ()
        for value in vector.coordinates():
            coordinates += (value * scalar,)

        return Vector.Vector(coordinates)
