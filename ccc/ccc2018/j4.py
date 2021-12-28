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

for i in range(len(matrix)):
    if i == 0:
        list1.append(matrix[i][0])
        list1.append(matrix[i][-1])
    if i == 2:
        list1.append(matrix[i][0])
        list1.append(matrix[i][-1])
# print(list1)
res = list1.index(min(list1))
# print(res)
# least = 100000

print(min(list1))
print(res)
if res == 0:
    # right
    # print(0)
    answer = matrix

elif res == 1:
    # print(1)
    answer = list(map(list, zip(*matrix)))[::-1]
    answer = list(map(list, zip(*answer)))[::-1]
    answer = list(map(list, zip(*answer)))[::-1]
    answer = list(map(list, zip(*answer)))[::-1]
    answer = list(map(list, zip(*answer)))[::-1]
    # answer = list(map(list, zip(*answer)))[::-1]
elif res == 2:
    # right
    # print(2)
    answer = list(map(list, zip(*matrix)))[::-1]
    answer = list(map(list, zip(*answer)))[::-1]
    answer = list(map(list, zip(*answer)))[::-1]
elif res == 3:
    print(3)
    # print(matrix)
    answer = list(map(list, zip(*matrix)))[::-1]
    answer = list(map(list, zip(*answer)))[::-1]

for ii in answer:
    for ii2 in range(N):
        print(int(ii[ii2]), end=" ")
    print()
