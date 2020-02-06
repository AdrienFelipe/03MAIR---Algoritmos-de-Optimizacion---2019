from matrix import Matrix
from matrix import MatrixException


class MatrixDeterminant:

    @staticmethod
    def calculate(matrix: Matrix) -> float:
        MatrixDeterminant.__validate(matrix)

        if matrix.rows_dimension() is 1:
            return matrix.value_at(0, 0)

        determinant = 0
        # Select first row as reference.
        row = 0
        for column, value in enumerate(matrix.coordinates()[row]):
            sign = 1 if column % 2 is 0 else -1
            sub_matrix = matrix.sub_matrix(row, column)
            determinant += sign * value * MatrixDeterminant.calculate(sub_matrix)

        return determinant

    @staticmethod
    def __validate(matrix: Matrix) -> None:
        if matrix.rows_dimension() != matrix.columns_dimension():
            raise MatrixException.NotSquareException('Matrix must be square')

    @staticmethod
    def sub_matrix(matrix: Matrix, removed_row: int, removed_column: int) -> Matrix:
        coordinates = ()
        for row, columns in enumerate(matrix.coordinates()):
            # Ignore input row.
            if row is removed_row:
                continue

            row_values = ()
            for column, value in enumerate(columns):
                # Ignore input column.
                if column is removed_column:
                    continue

                row_values += (value,)
            coordinates += (row_values,)

        return Matrix.Matrix(coordinates)
