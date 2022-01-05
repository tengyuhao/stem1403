"""
2018 J4
最小值
如果在左上角，则不旋转
如果在左下角，则右转90°一次
如果在右上角，则左转90°一次
如果在右下角，则右转90°二次，或左转90°二次
"""

N = int(input())
matrix = [[] for i in range(N)]
answer = []
# matrix = [['3', '7', '9'], ['2', '5', '6'], ['1', '3', '4']]
for i in range(N):
    line = input().split(" ")
    matrix[i] = line

new_list = []
for i in range(len(matrix)):
    if i == 0:
        new_list.append(matrix[i][0])
        new_list.append(matrix[i][-1])
    if i == N-1:
        new_list.append(matrix[i][0])
        new_list.append(matrix[i][-1])

# print(new_list)
res = new_list.index(min(new_list))
# print(res)
answer = matrix

if res == 0:
    # right
    # print(0)
    answer = answer

if res == 1:
    # print("1")
    for i in range(5):
        answer = list(map(list, zip(*answer)))[::-1]
if res == 2:
    # print("2")
    for i in range(3):
        answer = list(map(list, zip(*answer)))[::-1]
if res == 3:
    # print(3)
    answer = list(map(list, zip(*answer)))[::-1]
    answer = list(map(list, zip(*answer)))[::-1]
# print(answer)

for ii in answer:
    for ii2 in range(N):
        print(int(ii[ii2]), end=" ")
    print()
