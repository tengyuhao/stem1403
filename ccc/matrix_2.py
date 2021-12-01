"""
generate matrix
2D array
"""


# 1.5
n = 3
m = 4
matrix = [[0]*n]*m
print(matrix)
# matrix[1] = 99

matrix[1] = [1, 2, 3]
# 1.6
n = 3
# matrix = [0 for i in range(n) for j in range(n)]
# print(matrix)

matrix = [[0 for i in range(n)] for j in range(n)]
print(matrix)
