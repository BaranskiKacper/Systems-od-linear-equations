import copy
from math import sin, sqrt


def create_matrix(a1, a2, a3, N):
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            if i == j:
                row.append(a1)
            elif i - 1 <= j <= i + 1:
                row.append(int(a2))
            elif i - 2 <= j <= i + 2:
                row.append(int(a3))
            else:
                row.append(int(0))
        matrix.append(row)
    return matrix


def create_vector(f, N):
    return [sin(i * (f + 1)) for i in range(N)]


def fill(rows, cols, value):
    matrix = []
    for r in range(0, rows):
        matrix.append([value for _ in range(0, cols)])
    return matrix


def sub(a, b):
    return [a[i]-b[i] for i in range(len(a))]


def norm(vector):
    norm_res = 0.0
    for elem in vector:
        norm_res += pow(elem, 2)
    return sqrt(norm_res)


def dot(matrix, vector):
    length = len(matrix)
    length2 = len(matrix[0])
    multiplied = [0] * length
    for i in range(length):
        for j in range(length2):
            multiplied[i] += matrix[i][j] * vector[j]
    return multiplied
