"""
资源： 0.379s, 9.32 MB
最慢一次测试的运行时间 0.026s
最终得分： 15/15 (3.0/3 points)

time used : 5min
"""
N = int(input())
k = int(input())
res = N
multi = N
for i in range(k):
    multi = multi * 10
    # print(multi)
    res += multi
    # print(res)

print(res)