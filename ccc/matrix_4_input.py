
# 1.6
N = int(input())
# matrix = [0 for i in range(n) for j in range(n)]
# print(matrix)

matrix = [[] for i in range(N)]
print(matrix)

for i in range(N):
    line = input().split(" ")
    matrix[i] = line


print(matrix)