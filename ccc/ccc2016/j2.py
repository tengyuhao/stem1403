"""
2016 J2
资源： 0.304s, 9.46 MB
最慢一次测试的运行时间 0.026s
最终得分： 15/15 (3.0/3 points)
16 3 2 13
5 10 11 8
9 6 7 12
4 15 14 1
"""
# matrix = [[] for i in range(3) for j in range(3)]
res = 0
res2 = 0
res_list2 = []
matrix = [[] for i in range(4)]
res_list = []
condition = None
for i in range(4):
    line = input().split(" ")
    matrix[i] = line

# print(matrix)


for i in range(4):
    for i2 in range(4):
        res += int(matrix[i][i2])
        if i2 == 3:
            res_list.append(res)
    res = 0


# print(res_list)

line1 = matrix[0]
line2 = matrix[1]
line3 = matrix[2]
line4 = matrix[3]
ans = zip(line1, line2, line3, line4)
# print(list(ans))
ans_list = list(ans)
# print(ans_list)
for i3 in range(4):
    for i4 in range(4):
        res2 += int(ans_list[i3][i4])
        if i4 == 3:
            res_list2.append(res2)
    res2 = 0

# print(res_list2)
if max(res_list) == max(res_list2) == min(res_list) == min(res_list2):
    print("magic")
else:
    print("not magic")
