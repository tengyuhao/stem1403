"""
2016 J1
资源： 0.144s, 9.23 MB
最慢一次测试的运行时间 0.021s
最终得分： 15/15 (3.0/3 points)
"""
w = 0
l = 0

for i in range(6):
    V = input()
    if V == "W":
        w += 1
    if V == "L":
        l += 1

if w == 6 or w == 5:
    print(1)
if w == 3 or w == 4:
    print(2)
if w == 1 or w == 2:
    print(3)
if l == 6:
    print(-1)