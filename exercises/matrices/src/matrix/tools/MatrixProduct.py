from matrix import Matrix
from matrix import MatrixException


class MatrixProduct:

    @staticmethod
    def calculate(a: Matrix, b: Matrix) -> Matrix:
        MatrixProduct.__validate(a, b)

        coordinates = ()
        # Loop though matrix A rows.
        for row, columns in enumerate(a.coordinates()):
            row_values = ()
            # Loop though matrix B columns.
            for column in range(b.columns_dimension()):
                result_value = 0
                # For each value in matrix A row.
                for position, a_value in enumerate(columns):
                    # Fetch matrix B value in corresponding column.
                    b_value = b.coordinates()[position][column]
                    result_value += a_value * b_value
                # Result row.
                row_values += (result_value,)
            coordinates += (row_values,)

        return Matrix.Matrix(coordinates)

    @staticmethod
    def __validate(a: Matrix, b: Matrix) -> None:
        if a.columns_dimension() != b.rows_dimension():
            raise MatrixException.DimensionException('Matrices inner dimensions must be equal')
