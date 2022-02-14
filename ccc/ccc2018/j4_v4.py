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

list1 = []
for i in range(len(matrix)):
    if i == 0:
        list1.append(matrix[i][0])
        list1.append(matrix[i][-1])
    if i == 2:
        list1.append(matrix[i][0])
        list1.append(matrix[i][-1])
# print(list1)
res = list1.index(min(list1))


if res == 0:
    # right
    # print(0)
    output(matrix)
if res == 1:
    # print("1")
    m = rotateLeft(matrix)
    output(m)
if res == 2:
    m = rotateRight(matrix)
    output(m)
if res == 3:
    m = rotateLeft(rotateLeft(matrix))
    output(m)
    # print("d")