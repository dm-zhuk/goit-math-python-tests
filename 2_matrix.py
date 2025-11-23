import numpy as np

A = np.array([[2, 1, -1], [0, 1, -4]])
B = np.array([[-2, 1, 0], [-3, 2, 2]])
C = np.array([[3, -4, 2], [-3, 2, 2]])
# print(A + B + C)


A1 = np.array([[2, 1, -1], [0, 1, -4], [0, 1, -2]])
B1 = np.array([[-2, 1, 0], [-3, 2, 2], [-4, 1, 5]])
# print(A1 - B1)


A2 = np.array([[2, 1, -1], [0, 1, -4]])
# print(3 * A2)

# Pозв'язання для визначення добутку матриць
a = np.array([[1, 1], [1, 1]])
b = np.array([[1, 1], [1, 1]])
total = a.dot(b)
# print(total)


a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
total = a.dot(b)
# print(total)
# [[19 22]
#  [43 50]]

# ==self 1==
C1 = np.array([[4, 6], [3, 2]])
D1 = np.array([[8, 2], [3, 1]])
total = C1.dot(D1)
print(total)
# [[50 14]
# [30  8]]


# Define the matrices C and D using NumPy arrays
F = np.array([[4, 6], [3, 2]])

G = np.array([[8, 2], [3, 1]])

# Perform matrix multiplication using the @ operator (or np.dot())
# The @ operator is the standard for matrix multiplication in NumPy (Python 3.5+)
P = F @ G

# Print the result
print("--- Matrix F ---")
print(F)
print("\n--- Matrix G ---")
print(G)
print("\n--- Product P = F @ G ---")
print(P)

# Verify the type of the result (it's a NumPy array)
# print(type(P))
