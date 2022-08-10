import time

from MatrixMethods import *

norm_res = pow(10, -9)


def jacobi(a, b, N):
    start_time = time.time()
    length = len(a)
    iter_count = 0
    x = [0] * length

    while 1:
        for i in range(length):
            x[i] = b[i]
            for j in range(length):
                if i != j:
                    x[i] -= a[i][j] * x[j]
            x[i] /= a[i][i]
        res = sub(dot(a, x), b)

        if norm(res) < norm_res:
            break
        iter_count += 1
    time_taken = time.time() - start_time
    print(" For N = ", N)
    print(" Jacobi iterative method ")
    print("     Time(s): ", time_taken)
    print("     Number of iterations: ", iter_count)
    print("---------------------------")
    return time_taken


def gauss_seidel(a, b, N):
    start_time = time.time()
    length_b = len(b)
    length = len(a)
    iter_counter = 0
    known_x = [0] * length_b

    while 1:
        iter_counter += 1
        for i in range(length):
            new_x = b[i]
            for j in range(length):
                if i != j:
                    new_x -= a[i][j] * known_x[j]
            new_x /= a[i][i]
            known_x[i] = new_x
        residuum = sub(dot(a, known_x), b)
        if norm(residuum) < norm_res:
            break

    time_taken = time.time() - start_time
    print(" For N = ", N)
    print(" Gauss-Seidel iterative method ")
    print("     Time(s) : ", time_taken)
    print("     Number of iterations : ", iter_counter)
    print("---------------------------")
    return time_taken
