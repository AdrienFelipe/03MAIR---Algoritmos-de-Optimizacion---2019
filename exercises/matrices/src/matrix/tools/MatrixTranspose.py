from matrix import Matrix


class MatrixTranspose:
    @staticmethod
    def calculate(matrix: Matrix) -> Matrix:
        # Initialize coordinates a list for setup convenience.
        coordinates = []
        for row, columns in enumerate(matrix.coordinates()):
            for column, value in enumerate(columns):
                # Initialize rows on first iteration.
                if row is 0:
                    coordinates.append(())
                # Fill up the transposed values.
                coordinates[column] += (value,)

        return Matrix.Matrix(tuple(coordinates))
