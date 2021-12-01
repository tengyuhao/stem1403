#
# # 1.6
# N = int(input())
# # matrix = [0 for i in range(n) for j in range(n)]
# # print(matrix)
#
# matrix = [[] for i in range(N)]
# print(matrix)
#
# for i in range(N):
#     line = input().split(" ")
#     matrix[i] = line
#
#
# print(matrix)

m1 = [['1', '2', '3', '4'], ['3', '4', '5', '6']]
for i in range(len(m1)):

    for i2 in range(len(m1[i])):
        print(m1[i][i2])
        m1[i][i2] = int(m1[i][i2])

#
m1pro = ['3', '4', '5', '6']
print(list(map(int, m1pro)))

#
m1 = [['1', '2', '3', '4'], ['3', '4', '5', '6']]
for i in range(len(m1)):
    m1[i] = list(map(int, m1[i]))

print(m1)