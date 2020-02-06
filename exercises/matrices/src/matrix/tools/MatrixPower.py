import numpy

from matrix import Matrix
from matrix.tools.MatrixFactory import MatrixFactory


class MatrixPower:

    @staticmethod
    def sequential(matrix: Matrix, power: int) -> Matrix:
        """Elevate A to power value by matrix product"""
        a = matrix
        for i in range(1, power):
            a = a.product(matrix)

        return a

    @staticmethod
    def diagonalized(matrix: Matrix, power: int, diagonal_only: bool) -> Matrix:
        """Elevate matrix A to power value by diagonalization"""
        # Extract diagonalization values and vectors.
        eigen_values, eigen_vectors = numpy.linalg.eig(matrix.to_list())
        # Build diagonal matrix (D) and elevate it to k (D^k).
        diagonal_matrix = MatrixPower.__build_diagonal_matrix(matrix, eigen_values)
        diagonal_powered = MatrixPower.__power_diagonal_matrix(diagonal_matrix, power)

        # Exit if we only want to power the diagonal matrix.
        if diagonal_only is True:
            return diagonal_powered

        # Build eigen matrix (P).
        eigen_matrix = MatrixFactory.from_list(list(eigen_vectors))

        # Power by diagonalization = P · D^k · P⁻¹
        return eigen_matrix.product(diagonal_powered).product(eigen_matrix.inverse())

    @staticmethod
    def __build_diagonal_matrix(matrix: Matrix, eigen_values: numpy.ndarray) -> Matrix:
        coordinates = ()
        for row in range(matrix.rows_dimension()):
            row_values = ()
            for column in range(matrix.columns_dimension()):
                value = eigen_values[row] if row == column else 0
                row_values += (value,)
            coordinates += (row_values,)

        return Matrix.Matrix(coordinates)

    @staticmethod
    def __power_diagonal_matrix(matrix: Matrix, power: int) -> Matrix:
        coordinates = ()
        for row, columns in enumerate(matrix.coordinates()):
            row_values = ()
            for column, value in enumerate(columns):
                value = value ** power if row is column else 0
                row_values += (value,)
            coordinates += (row_values,)

        return Matrix.Matrix(coordinates)
