from matrix.Matrix import Matrix

# Inputs:
coordinates = ((-5, -2, 1), (-4, 3, 5,), (6, 0, 2))

print('\n# How to calculate the inverse of a matrix\n')
try:
    a = Matrix(coordinates)
    a.print('            A =')
except Exception as exception:
    print('Cannot create matrix A:')
    print(str(exception))
    quit()

# --------------------------------
# 6.a ----------------------------
print('- Matrix determinant')
try:
    # noinspection PyUnboundLocalVariable
    det = a.determinant()
    print('       det(A) =', det)
    print('')
except Exception as exception:
    print('Cannot calculate determinant of A:')
    print(str(exception))
    quit()

# --------------------------------
# 6.b ----------------------------
print('- Cofactor matrix of A')
try:
    c = a.cofactor()
    c.print('            C =')
except Exception as exception:
    print('Cannot calculate comatrix:')
    print(str(exception))
    quit()

# --------------------------------
# 6.c ----------------------------
print('- Matrix transpose')
try:
    # noinspection PyUnboundLocalVariable
    ct = c.transpose()
    ct.print('           Cᵀ =')
except Exception as exception:
    print('Cannot calculate transpose of C:')
    print(str(exception))
    quit()

# --------------------------------
# 6.d ----------------------------
print('- Matrix inverse')
try:
    # Calculate the inverse to catch any exception from the validation.
    i = a.inverse()
    # noinspection PyUnboundLocalVariable
    ct.multiply(1 / det).round(2).print('   1/det · Cᵀ =')
    i.round(2).print('          A⁻¹ =')
except Exception as exception:
    print('Cannot calculate inverse of A:')
    print(str(exception))
    quit()

# --------------------------------
# 6.e ----------------------------
print('- Validation')
try:
    # noinspection PyUnboundLocalVariable
    a.product(i).round(2).print('        A·A⁻¹ =')
    i.product(a).round(2).print('        A⁻¹·A =')
except Exception as exception:
    print(str(exception))
    quit()
