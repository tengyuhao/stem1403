"""
generate matrix
2D array
"""

# 1.1
list1 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(list1)

# for i in range(4):
#     for i2 in list1:
#         print(i2, end="     ")
#         if i2 == 3:
#             print()

# 1.2
matrix = []
line1 = [1, 2, 3]
line2 = [1, 2, 3]
line3 = [1, 2, 3]

matrix.append(line1)
matrix.append(line2)
matrix.append(line3)
print(matrix)

# 1.3
# error

# 1.4
matrix = []
line1 = [1, 2, 3]
line2 = [1, 2, 3]
line3 = [1, 2, 3]
for i in range(3):
    line1 = input().split(" ")
    matrix.append(line1)

# 1.5
n = 3
matrix = [0]*3
print(matrix)
matrix[1] = 99

# 1.6
n = 3
matrix = [0 for i in range(n)]
print(matrix)
