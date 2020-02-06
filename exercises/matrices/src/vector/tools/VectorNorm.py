from vector import Vector


class VectorNorm:

    @staticmethod
    def calculate(vector: Vector, p: int) -> float:
        """
        Calculates a generalized form of vector norm, where:
         - p = -1: Maximum norm
         - p = 0: Zero norm (yet to be implemented)
         - p = 1: Taxicab norm
         - p = 2: Euclidean norm
         - p = Z
        """
        # Infinite norm or max norm
        if p < 0:
            return max(vector.coordinates())

        # TODO: Zero norm, to be implemented
        if p == 0:
            return 0

        # p norm
        norm = 0
        for value in vector.coordinates():
            norm += value ** p

        return norm ** (1 / p)
