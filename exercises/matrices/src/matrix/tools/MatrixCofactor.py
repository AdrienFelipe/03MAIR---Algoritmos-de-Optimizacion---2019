from matrix import Matrix


class MatrixCofactor:
    @staticmethod
    def calculate(matrix: Matrix) -> Matrix:
        coordinates = ()
        for row in range(matrix.rows_dimension()):
            row_sign = 1 if row % 2 is 0 else -1
            row_values = ()
            for column in range(matrix.columns_dimension()):
                column_sign = 1 if column % 2 is 0 else -1
                minor = matrix.sub_matrix(row, column)
                value = row_sign * column_sign * minor.determinant()
                row_values += (value,)

            coordinates += (row_values,)

        return Matrix.Matrix(coordinates)
