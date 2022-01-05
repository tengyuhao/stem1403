"""
2020 J1
资源： 0.382s, 9.32 MB
最慢一次测试的运行时间 0.026s
最终得分： 15/15 (3.0/3 points)
"""

S = int(input())
M = int(input())
L = int(input())

condition = 1 * S + 2 * M + 3 * L
if condition >= 10:
    print("happy")
else:
    print("sad")