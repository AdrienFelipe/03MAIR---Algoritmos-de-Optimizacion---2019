from matrix import Matrix


class MatrixOutput:

    @staticmethod
    def to_list(matrix: Matrix) -> list:
        values = []
        for row, columns in enumerate(matrix.coordinates()):
            values += [list(columns), ]

        return values

    @staticmethod
    def print(matrix: Matrix, text: str) -> None:
        for row, columns in enumerate(matrix.coordinates()):
            print(text if row is 0 else ' ' * len(text), columns)
        print('')
