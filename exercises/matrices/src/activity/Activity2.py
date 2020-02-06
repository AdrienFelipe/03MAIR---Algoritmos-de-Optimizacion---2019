from requirements import vecnorm
from requirements.vecdot import vecdot
from vector.Vector import Vector

# --------------------------------
# 2.a.1 --------------------------
print('\n# Exercise 2.a: Infinite norm or max norm')

# Inputs:
v = Vector((1.3, 2.2, 3.1))

print(' v =', v.coordinates())
print(' max_norm(v) =', vecnorm.max_norm(v))

# 2.a.2 ----------------------------
print('\n# Exercise 2.a: Taxicab or Manhattan norm')

# Inputs:
v = Vector((1.3, 2.2, 3.1))

print(' v =', v.coordinates())
print(' taxicab_norm(v) =', vecnorm.taxicab_norm(v))

# --------------------------------
# 2.a.3 --------------------------
print('\n# Exercise 2.a: Euclidean norm')

# Inputs:
v = Vector((13, 56))

print(' v =', v.coordinates())
print(' euclidean_norm(v) =', vecnorm.euclidean_norm(v))

# --------------------------------
# 2.b ----------------------------
print('\n# Exercise 2.b: projection·orthogonal')

# Inputs:
u = Vector.random(3)
v = Vector.random(3)

print(' v =', v.coordinates())
print(' u =', u.coordinates())
print('')

p = u.projection_on(v)
o = u.orthogonal_on(v)
print('u projection on v:')
print(' p =', p.coordinates())
print('u orthogonal on v:')
print(' o =', o.coordinates())
print('')
print('Vector product of projection and orthogonal:')
print(' p·o =', round(vecdot(p, o), 10))

# --------------------------------
# -------------------------------
print('')
