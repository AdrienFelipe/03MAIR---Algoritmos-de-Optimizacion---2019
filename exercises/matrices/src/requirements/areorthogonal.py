from vector.Vector import Vector


# Whether two vectors are orthogonal.
def areorthogonal(x: Vector, y: Vector) -> bool:
    return x.product(y) == 0
