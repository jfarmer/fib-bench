import numpy as np


def fib_matrix(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    M = np.array([[1, 1], [1, 0]], dtype=object)
    result = np.linalg.matrix_power(M, n - 1)
    return int(result[0, 0])
