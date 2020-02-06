from matrix.Matrix import Matrix
from matrix.tools.MatrixFactory import MatrixFactory

# --------------------------------
# 5.a ----------------------------
print('\n# Extra 5.a: Identity product')

# Inputs:
a = Matrix(((5, -2,), (-4, 5,), (6, 5)))

a.print('   A =')

i2 = MatrixFactory.identity(a.columns_dimension())
i2.print('   I₂ =')
try:
    a.product(i2).print(' A·I₂ =')
except Exception as exception:
    print(str(exception))

i3 = MatrixFactory.identity(a.rows_dimension())
i3.print('   I₃ =')
try:
    i3.product(a).print(' I₃·A =')
except Exception as exception:
    print(str(exception))
