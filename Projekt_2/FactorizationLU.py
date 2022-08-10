import time

from MatrixMethods import *


def factorization_LU(a, b, N):
    start_time = time.time()
    length = len(a)
    L = fill(length, length, 1)
    U = fill(length, length, 0)
    x = [1.0] * length
    y = [0] * length

    # Tworzymy macierze L i U, takie, że: LUx = b
    for i in range(length):
        for j in range(i + 1):
            U[j][i] += a[j][i]
            for k in range(j):
                U[j][i] -= L[j][k] * U[k][i]

        for j in range(i + 1, length):
            for k in range(i):
                L[j][i] -= L[j][k] * U[k][i]
            L[j][i] += a[j][i]
            L[j][i] /= U[i][i]

    # Rozwiązujemy układ równań: Ly = b za pomocą podstawiania wprzód
    for j in range(length):
        value = b[j]
        for i in range(j):
            value -= L[j][i] * y[i]
        y[j] = value / L[j][j]

    # Rozwiązujemy układ równań: Ux = y za pomocą podstawiania wstecz
    for j in range(length - 1, -1, -1):
        value = y[j]
        for i in range(j + 1, length):
            value -= U[j][i] * x[i]
        x[j] = value / U[j][j]

    res = sub(dot(a, x), b)
    time_taken = time.time() - start_time
    print(" For N = ", N)
    print(" LU factorization method ")
    print("     Time(s): ", time_taken)
    print("     Residuum norm: ", norm(res))
    print("---------------------------")
    return time_taken
