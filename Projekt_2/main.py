
from matplotlib import pyplot
from FactorizationLU import *
from IterationMethods import *


if __name__ == "__main__":
    N_A = 913
    d = 3
    c = 1
    e = 6
    f = 2
    N = [100, 500, 1000, 2000, 3000]
    jacobi_time_taken = []
    gauss_seidel_time_taken = []
    LU_time_taken = []

    # Zadanie A
    A = create_matrix(e+5, -1, -1, N_A)
    b = create_vector(f, N_A)

    # Zadanie B
    jacobi(A, b, N_A)
    gauss_seidel(A, b, N_A)

    # Zadanie C
    C = create_matrix(3, -1, -1, N_A)
    jacobi(C, b,N_A)
    gauss_seidel(C, b, N_A)

    # Zadanie D
    factorization_LU(C, b, N_A)

    # Zadanie E
    for number_of_variables in N:
        A = create_matrix(e+5, -1, -1, number_of_variables)
        b = create_vector(f, number_of_variables)

        jacobi_time_taken.append(jacobi(A, b, number_of_variables))
        gauss_seidel_time_taken.append(gauss_seidel(A, b, number_of_variables))
        LU_time_taken.append(factorization_LU(A, b, number_of_variables))

    pyplot.plot(N, jacobi_time_taken, label="Jacobi", color="blue")
    pyplot.plot(N, gauss_seidel_time_taken, label="Gauss-Seidel", color="red")
    pyplot.plot(N, LU_time_taken, label="LU", color="green")
    pyplot.legend()
    pyplot.grid(True)
    pyplot.xlabel('Number of unknown variables')
    pyplot.ylabel('Time taken (s)')
    pyplot.title('Time dependence on the number of unknowns')
    pyplot.show()
