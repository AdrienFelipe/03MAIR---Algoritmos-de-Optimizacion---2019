import numpy as np


def create(n: int):
    # Matriz aleatoria con valores comprendidos entre 0 y 1.
    A = np.random.rand(n, n)

    # Hago simétrica la matriz aleatoria generada anteriormente.
    # Garantiza que la matriz es diagonalizable.
    for i in range(n):
        for j in range(i + 1, n):
            A[i, j] = A[j, i]

    # Calculo la suma de los elementos de cada fila y me quedo con la máxima.
    maxrow = 0
    for i in range(n):
        row = 0
        for j in range(n):
            row = row + A[i, j]
        if row > maxrow:
            maxrow = row

    # Divido todas las entradas de la matriz por el valor anterior.
    # Garantiza que los valores propios se encuentran entre 0 y 1.
    for i in range(n):
        for j in range(n):
            A[i, j] = A[i, j] / maxrow

    return A
