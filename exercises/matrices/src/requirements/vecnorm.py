from vector.Vector import Vector


def max_norm(vector: Vector) -> float:
    return vector.norm(-1)


def taxicab_norm(vector: Vector) -> float:
    return vector.norm(1)


def euclidean_norm(vector: Vector) -> float:
    return vector.norm(2)
