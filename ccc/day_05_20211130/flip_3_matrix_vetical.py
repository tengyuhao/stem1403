"""
horizontally flipping
"""

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

m = list.copy(matrix)
for i in range(len(m)):
    m[i].reverse()

print(matrix)
print(m)