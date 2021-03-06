"""
2018 J4
最小值
如果在左上角，则不旋转
如果在左下角，则右转90°一次
如果在右上角，则左转90°一次
如果在右下角，则右转90°二次，或左转90°二次

"""


def rotateLeft(matrix):
    # matrix[:] = map(list, zip(*matrix))[::-1]
    matrix[:] = map(list, zip(*matrix))
    return matrix[::-1]


def rotateRight(matrix):
    matrix[:] = map(list, zip(*matrix[::-1]))
    return matrix


N = int(input())
matrix = [[] for i in range(N)]
answer = []
# matrix = [['3', '7', '9'], ['2', '5', '6'], ['1', '3', '4']]
for i in range(N):
    line = input().split(" ")
    matrix[i] = line

a = matrix[0][0]
b = matrix[0][N-1]
c = matrix[N-1][0]
d = matrix[N-1][N-1]

res = min(a,b,c,d)

if a == res:
    # right
    # print(0)
    m = matrix
if b == res:
    # print("1")
    m = rotateLeft(matrix)
if c == res:

    m = rotateRight(matrix)
if d == res:
    m = rotateLeft(rotateLeft(matrix))
    # print("d")

# print(m)
for line in m:
    for num in line:
        print(num, end=" ")
    print()
