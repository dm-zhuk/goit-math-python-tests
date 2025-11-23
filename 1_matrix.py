"""import numpy as np


# Створення одиничної матриці розміром 4x4
identity_matrix = np.eye(4)

print(identity_matrix)"""


def print_diagonals(matrix):
    rows, cols = len(matrix), len(matrix[0])

    if rows != cols:
        print("Матриця не є квадратною. Головна та побічна діагоналі не визначені.")
        return

    main_diagonal = [matrix[i][i] for i in range(rows)]
    anti_diagonal = [matrix[i][cols - 1 - i] for i in range(rows)]

    print("Головна діагональ:", main_diagonal)
    print("Побічна діагональ:", anti_diagonal)


# Приклад використання
matrix_example = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


print_diagonals(matrix_example)

# import numpy as np

# A = np.array([[2, 1, -1], [0, 1, -4]])
# B = np.array([[-2, 1, 0], [-3, 2, 2]])
# print(A + B)
