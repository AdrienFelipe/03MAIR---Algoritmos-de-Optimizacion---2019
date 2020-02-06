from vector.Vector import Vector
from requirements.areorthogonal import areorthogonal
from requirements.vecdot import vecdot

# --------------------------------
# 1.a ----------------------------
print('\n# Exercise 1.a: vectod')

# Inputs:
x = Vector((4, 5, 1))
y = Vector((2, 2, 8))

print(' x =', x.coordinates())
print(' y =', y.coordinates())
print(' vecdot(x, y) =', vecdot(x, y))

# --------------------------------
# 1.b ----------------------------
print('\n# Exercise 1.b: areorthogonal')

# Find two orthogonal vectors:
# Be x(a, b) and y(c, d) orthogonal
# <=> x·y = 0
#
# So x·y = a*c + b*d = 0
# => a = -b*d / c, \forall c \neq 0
# Suppose b=3, c=1, d=2
# => a = -3 * 2 / 1 = -6
#
# => x(-6, 3), y(1, 2)

# Inputs:
x = Vector((-6, 3))
y = Vector((1, 2))

print(' x =', x.coordinates())
print(' y =', y.coordinates())
print(' areorthogonal(x, y) =', areorthogonal(x, y))

# --------------------------------
# --------------------------------
print('')
