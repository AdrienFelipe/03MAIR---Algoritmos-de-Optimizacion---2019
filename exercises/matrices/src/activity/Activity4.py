import time
from matrix.Matrix import Matrix
from matrix.tools.MatrixFactory import MatrixFactory

# --------------------------------
# 4.a ----------------------------
print('\n# Exercise 4.a: Matrix sequential power')

# Inputs: Matrix A must be square.
a = Matrix(((5, -2,), (-4, 5,)))
power = 5

a.print('   A =')
try:
    # Elevate A to the power value using matrices product.
    b = a.power_sequential(power)
    b.print(' A^' + str(power) + ' =')
except Exception as exception:
    print(str(exception))

# --------------------------------
# 4.b ----------------------------
print('\n# Exercise 4.b: Matrix diagonal power')

# Inputs: Matrix A must be square.
a = Matrix(((5, -2,), (-4, 5,)))
power = 5

a.print('   A =')
try:
    # Elevate A to the power value using matrix diagonalization.
    b = a.power_diagonalized(power).round(10)
    b.print(' A^' + str(power) + ' =')
except Exception as exception:
    print(str(exception))

# --------------------------------
# 4.c ----------------------------
print('\n# Exercise 4.c: Matrix power comparison')

# Inputs:
dimension = 100
power = 10

a = MatrixFactory.random(dimension)

# Sequential power time.
print('')
print('Calculating random A' + str(dimension) + 'x' + str(dimension) + ' ** ' + str(power) + ' sequentially')
start_time = time.time()
a.power_sequential(power)
print("Calculated in: %s seconds" % round(time.time() - start_time))

# Diagonal power time.
print('')
print('Calculating random A' + str(dimension) + 'x' + str(dimension) + ' ** ' + str(power) + ' by diagonalization')
start_time = time.time()
# Only calculates the power of the diagonal matrix.
a.power_diagonalized(power, diagonal_only=True)
print("Calculated in: %s seconds" % round(time.time() - start_time))

# -------------------------------
# -------------------------------
print('')
