"""
2018 J4
最小值
如果在左上角，则不旋转
如果在左下角，则右转90°一次
如果在右上角，则左转90°一次
如果在右下角，则右转90°二次，或左转90°二次
资源： 0.339s, 10.00 MB
最慢一次测试的运行时间 0.028s
最终得分： 15/15 (5.0/5 points)
"""


def rotateLeft(matrix):
    # matrix[:] = map(list, zip(*matrix))[::-1]
    matrix[:] = map(list, zip(*matrix))
    return matrix[::-1]


def rotateRight(matrix):
    matrix[:] = map(list, zip(*matrix[::-1]))
    return matrix

def output(matrix):
    for line in matrix:
        for num in line:
            print(num, end=" ")
        print()


N = int(input())
matrix =[[0 for i in range(N)] for j in range(N)]
answer = []
# matrix = [['3', '7', '9'], ['2', '5', '6'], ['1', '3', '4']]
for i in range(N):
    line = input().split(" ")
    line = list(map(int, line))
    matrix[i] = line

a = matrix[0][0]
b = matrix[0][N-1]
c = matrix[N-1][0]
d = matrix[N-1][N-1]

res = min(a,b,c,d)

if a == res:
    # right
    # print(0)
    output(matrix)
if b == res:
    # print("1")
    m = rotateLeft(matrix)
    output(m)
if c == res:
    m = rotateRight(matrix)
    output(m)
if d == res:
    m = rotateLeft(rotateLeft(matrix))
    output(m)
    # print("d")
