from __future__ import annotations

from matrix.tools.MatrixCofactor import MatrixCofactor
from matrix.tools.MatrixDeterminant import MatrixDeterminant
from matrix.tools.MatrixFactory import MatrixFactory
from matrix.tools.MatrixInverse import MatrixInverse
from matrix.tools.MatrixMultiplication import MatrixMultiplication
from matrix.tools.MatrixOutput import MatrixOutput
from matrix.tools.MatrixPower import MatrixPower
from matrix.tools.MatrixProduct import MatrixProduct
from matrix.tools.MatrixSum import MatrixSum
from matrix.tools.MatrixTranspose import MatrixTranspose


class Matrix:
    """
    Coordinates are expected as tuples in the form:
    - rows: tuple
     -- columns: tuple

     ie:
        Matrix: 1 2
                5 4

     -> Matrix(((1, 2), (5, 4)))
    """

    def __init__(self, coordinates: tuple):
        # Make sure Matrix inputs are valid.
        MatrixFactory.validate(coordinates)
        # Setup Matrix properties.
        self.__coordinates = coordinates

    def coordinates(self) -> tuple:
        return self.__coordinates

    def value_at(self, row: int, column: int) -> float:
        return self.__coordinates[row][column]

    def print(self, text: str = '') -> None:
        MatrixOutput.print(self, text)

    def to_list(self) -> list:
        return MatrixOutput.to_list(self)

    def rows_dimension(self) -> int:
        return len(self.__coordinates)

    def columns_dimension(self) -> int:
        return len(self.__coordinates[0])

    def multiply(self, scalar: float) -> Matrix:
        return MatrixMultiplication.calculate(self, scalar)

    def add(self, b: Matrix) -> Matrix:
        return MatrixSum.add(self, b)

    def subtract(self, b: Matrix) -> Matrix:
        return MatrixSum.subtract(self, b)

    def product(self, b: Matrix) -> Matrix:
        return MatrixProduct.calculate(self, b)

    def power_sequential(self, power: int) -> Matrix:
        return MatrixPower.sequential(self, power)

    def power_diagonalized(self, power: int, diagonal_only: bool = False) -> Matrix:
        return MatrixPower.diagonalized(self, power, diagonal_only)

    def sub_matrix(self, row: int, column: int) -> Matrix:
        return MatrixDeterminant.sub_matrix(self, row, column)

    def determinant(self) -> float:
        return MatrixDeterminant.calculate(self)

    def transpose(self) -> Matrix:
        return MatrixTranspose.calculate(self)

    def cofactor(self) -> Matrix:
        return MatrixCofactor.calculate(self)

    def inverse(self) -> Matrix:
        return MatrixInverse.calculate(self)

    def round(self, precision: int) -> Matrix:
        return MatrixFactory.round(self, precision)
