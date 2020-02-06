from matrix import MatrixException
from matrix.Matrix import Matrix

# --------------------------------
# 3.a ----------------------------
print('\n# Exercise 3.a: Matrix scalar multiplication')

# Inputs:
a = Matrix(((1, 2, 3), (4, 5, 6)))
scalar = 5

b = a.multiply(scalar)
a.print('   A =')
b.print(' ' + str(scalar) + '*A =')

# --------------------------------
# 3.b ----------------------------
print('\n# Exercise 3.b: Matrix addition')

# Inputs:
a = Matrix(((1, -2, 3), (-4, 5, 1)))
b = Matrix(((7, -4, 1), (-2, 0, 5)))

a.print('   A =')
b.print('   B =')

try:
    # Addition will throw an exception if matrices don't have equal dimensions.
    c = a.add(b)
    print(' Matrices A and B have the same dimensions:', a.rows_dimension(), 'x', a.columns_dimension())
    c.print(' A+B =')

except MatrixException.DimensionException:
    print(' Matrices A and B do not have the same dimensions')
    print(' and therefore cannot be added.')

# --------------------------------
# 3.c ----------------------------
print('\n# Exercise 3.c: Matrix product')

# Inputs:
a = Matrix(((5, -2, 3), (-4, 5, 1)))
b = Matrix(((7, -4), (-2, 0), (5, -7)))

a.print('   A =')
b.print('   B =')
print(' Matrices dimensions:')
print(' A:', a.rows_dimension(), 'x', a.columns_dimension())
print(' B:', b.rows_dimension(), 'x', b.columns_dimension())

try:
    # Product will throw an exception if matrices don't have compatible dimensions.
    c = a.product(b)
    print(' Matrices A and B have compatible dimensions')
    print('')
    c.print(' C = A·B =')

except MatrixException.DimensionException:
    print(' Matrices A and B do not have compatible dimensions')
    print(' and therefore their product cannot be calculated.')

# -------------------------------
# -------------------------------
print('')
