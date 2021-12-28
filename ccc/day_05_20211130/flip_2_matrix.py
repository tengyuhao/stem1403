"""
horizontally flipping
"""

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
# for i in range(len(matrix)):
#     inverse = len(matrix) // 2
#     change = matrix[i]
#     matrix[i] = matrix[inverse]
#     matrix[inverse] = change
#     print(matrix[inverse])
# print(matrix)

m = matrix[::-1]
print(m)
