from __future__ import annotations

from .tools.VectorSum import VectorSum
from .tools.VectorOrthogonal import VectorOrthogonal
from .tools.VectorMultiplication import VectorMultiplication
from .tools.VectorProjection import VectorProjection
from .tools.VectorFactory import VectorFactory
from .tools.VectorNorm import VectorNorm
from .tools.VectorProduct import VectorProduct


class Vector:
    def __init__(self, coordinates: tuple):
        self.__coordinates = coordinates

    @staticmethod
    def random(dimension: int) -> Vector:
        return VectorFactory.random(dimension)

    def coordinates(self) -> tuple:
        return self.__coordinates

    def dimension(self) -> int:
        return len(self.__coordinates)

    def scalar_multiplication(self, scalar: float) -> Vector:
        return VectorMultiplication.calculate(self, scalar)

    def add(self, y: Vector) -> Vector:
        return VectorSum.add(self, y)

    def subtract(self, y: Vector) -> Vector:
        return VectorSum.subtract(self, y)

    def product(self, y: Vector) -> float:
        return VectorProduct.calculate(self, y)

    def norm(self, p: int) -> float:
        return VectorNorm.calculate(self, p)

    def projection_on(self, y: Vector) -> Vector:
        return VectorProjection.calculate(self, y)

    def orthogonal_on(self, y: Vector) -> Vector:
        return VectorOrthogonal.calculate(self, y)
