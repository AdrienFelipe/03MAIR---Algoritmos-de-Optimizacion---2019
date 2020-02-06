from matrix import MatrixException
from matrix import Matrix


class MatrixFactory:

    @staticmethod
    def validate(coordinates: tuple) -> None:
        # Validate coordinates level 1.
        if type(coordinates) != tuple:
            raise MatrixException.CoordinatesTypeException('Row coordinates must be a tuple')

        # Validate coordinates level 2.
        for row in coordinates:
            # Validate type.
            if type(row) != tuple:
                raise MatrixException.CoordinatesTypeException('Column coordinates must be tuples')

            # Validate dimension.
            if len(coordinates[0]) != len(row):
                raise MatrixException.DimensionException('All columns must have the same dimension')

    @staticmethod
    def from_list(values: list) -> Matrix:
        coordinates = ()
        for row, columns in enumerate(values):
            row_values = ()
            for column, value in enumerate(columns):
                row_values += (value,)
            coordinates += (row_values,)

        return Matrix.Matrix(coordinates)

    @staticmethod
    def identity(dimension: int) -> Matrix:
        coordinates = ()
        for row in range(dimension):
            row_values = ()
            for column in range(dimension):
                value = 1 if row is column else 0
                row_values += (value,)
            coordinates += (row_values,)

        return Matrix.Matrix(coordinates)

    @staticmethod
    def round(matrix: Matrix, precision: int) -> Matrix:
        coordinates = ()
        for columns in matrix.coordinates():
            row_values = ()
            for value in columns:
                row_values += (round(value, precision),)
            coordinates += (row_values,)

        return Matrix.Matrix(coordinates)

    @staticmethod
    def random(dimension: int) -> Matrix:
        from requirements import pseudorandom_matrix
        coordinates = ()
        for row in pseudorandom_matrix.create(dimension):
            coordinates += (tuple(row),)

        return Matrix.Matrix(coordinates)
