from matrix import Matrix
from matrix import MatrixException


class MatrixInverse:
    @staticmethod
    def calculate(matrix: Matrix) -> Matrix:
        # Check whether matrix determinant is null.
        determinant = matrix.determinant()
        if determinant is 0:
            raise MatrixException.NullDeterminantException

        # Inverse of matrix A is: 1/det(A) · Adj(A)
        # Adjugate matrix Adj(A) is: the transpose of the cofactor matrix.
        return matrix.cofactor().transpose().multiply(1 / determinant)
