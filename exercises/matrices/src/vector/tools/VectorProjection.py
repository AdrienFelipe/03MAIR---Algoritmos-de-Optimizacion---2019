from vector import Vector


class VectorProjection:

    @staticmethod
    def calculate(x: Vector, y: Vector) -> Vector:
        """Calculate X projection on Y"""
        # TODO: make sure vector Y is not a point (null coordinates)
        ratio = x.product(y) / y.product(y)

        return y.scalar_multiplication(ratio)
