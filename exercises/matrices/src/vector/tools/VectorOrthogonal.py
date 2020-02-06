from vector import Vector


class VectorOrthogonal:

    @staticmethod
    def calculate(x: Vector, y: Vector) -> Vector:
        """Calculate X orthogonal on Y"""
        return x.subtract(x.projection_on(y))
