from matrix import Matrix


class MatrixMultiplication:
    @staticmethod
    def calculate(matrix: Matrix, scalar: float) -> Matrix:
        coordinates = ()
        for row, columns in enumerate(matrix.coordinates()):
            row_values = ()
            for column, value in enumerate(columns):
                row_values += (value * scalar,)
            coordinates += (row_values,)

        return Matrix.Matrix(coordinates)
