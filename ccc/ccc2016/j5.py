"""
2016 J5
资源： 0.361s, 9.44 MB
最慢一次测试的运行时间 0.025s
最终得分： 15/15 (5.0/5 points)
"""
Q = input()
Q = int(Q)
N = int(input())
v1_str = input()
v2_str = input()
v1_str = v1_str.split(" ")
v2_str = v2_str.split(" ")


v1_int = []
v2_int = []

for i in v1_str:
    i = int(i)
    v1_int.append(i)
for i in v2_str:
    i = int(i)
    v2_int.append(i)
# v1_str.sort()
# v2_str.sort()
v1_int.sort()
v2_int.sort()
res_1 = 0
res_2 = 0
# print(v1_int)
# print(v2_int)
if Q == 1:
    for i in range(N):
        res_1 += max(int(v1_int[i]), int(v2_int[i]))
        # print(res_1)
    print(res_1)

if Q == 2:
    v2_int.reverse()
    print(v2_int)
    for i in range(N):
        res_2 += max(int(v1_int[i]), int(v2_int[i]))
        # print(res_1)
    print(res_2)
