from matrix import Matrix
from matrix import MatrixException


class MatrixSum:

    @staticmethod
    def add(a: Matrix, b: Matrix) -> Matrix:
        # Validate input matrices.
        MatrixSum.__validate(a, b)
        # Add both matrices.
        coordinates = ()
        for row, columns in enumerate(a.coordinates()):
            row_values = ()
            for column, a_value in enumerate(columns):
                b_value = b.coordinates()[row][column]
                row_values += (a_value + b_value,)
            coordinates += (row_values,)

        return Matrix.Matrix(coordinates)

    @staticmethod
    def subtract(a: Matrix, b: Matrix) -> Matrix:
        # Subtract both matrices.
        return a.add(b.multiply(-1))

    @staticmethod
    def __validate(a: Matrix, b: Matrix) -> None:
        if a.columns_dimension() != b.columns_dimension():
            raise MatrixException.DimensionException('Matrices columns must be equal.')

        if a.rows_dimension() != b.rows_dimension():
            raise MatrixException.DimensionException('Matrices rows must be equal.')
