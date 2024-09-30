import numpy as np

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

A = np.array(a)

print(A.ndim)
print(A.shape)
print(A.size)

print(A[1][2])
print(A[0][0:2])

x = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
z = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])
y = np.array(x)
print(y)
print(y[0][0:2])
print(np.dot(x, z))