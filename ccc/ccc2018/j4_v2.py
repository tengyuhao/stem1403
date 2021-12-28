"""
2018 J4
"""

N = int(input())
matrix = [[] for i in range(N)]
list1 = []
answer = []
# matrix = [['3', '7', '9'], ['2', '5', '6'], ['1', '3', '4']]
for i in range(N):
    line = input().split(" ")
    matrix[i] = line
# print(matrix)

a = matrix[0][0]
b = matrix[0][N-1]
c = matrix[N-1][0]
d = matrix[N-1][N-1]

vertex = min(a, b, c, d)
# print(list1)
# print(res)
# least = 100000

# print(min(list1))
if a == vertex:
    # right
    # print(0)
    answer = matrix

elif b == vertex:
    # print(1)
    answer = list(map(list, zip(*matrix)))[::-1]
    answer = list(map(list, zip(*answer)))[::-1]
    answer = list(map(list, zip(*answer)))[::-1]
    answer = list(map(list, zip(*answer)))[::-1]
    answer = list(map(list, zip(*answer)))[::-1]
    # answer = list(map(list, zip(*answer)))[::-1]
elif c == vertex:
    # right
    # print(2)
    answer = list(map(list, zip(*matrix)))[::-1]
    answer = list(map(list, zip(*answer)))[::-1]
    answer = list(map(list, zip(*answer)))[::-1]
elif d == vertex:
    print(3)
    # print(matrix)
    answer = list(map(list, zip(*matrix)))[::-1]
    answer = list(map(list, zip(*answer)))[::-1]

for ii in answer:
    for ii2 in range(N):
        print(int(ii[ii2]), end=" ")
    print()
