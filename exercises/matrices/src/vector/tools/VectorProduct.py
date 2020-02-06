from vector import Vector
from vector.VectorException import VectorDimensionException


# Calculate two vectors scalar product.
class VectorProduct:

    @staticmethod
    def calculate(x: Vector, y: Vector) -> float:
        # Make sure a vector product can be calculated.
        VectorProduct.__validate(x, y)

        # Calculate x·y scalar product.
        result = 0.
        for key, x_value in enumerate(x.coordinates()):
            y_value = y.coordinates()[key]
            result += x_value * y_value

        return result

    @staticmethod
    def __validate(x: Vector, y: Vector) -> None:
        # Vectors must have the same dimensions to calculate a product.
        if not x.dimension() == y.dimension():
            raise VectorDimensionException('Vectors must have the same dimension.')
