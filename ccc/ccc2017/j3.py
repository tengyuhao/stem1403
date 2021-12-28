"""
资源： 0.431s, 9.28 MB
最慢一次测试的运行时间 0.026s
最终得分： 15/15 (3.0/3 points)
"""

a = input()
b = input()

ax, ay = a.split(" ")
bx, by = b.split(" ")

electrical = int(input())


t_min = abs(int(ax) - int(bx)) + abs(int(ay) - int(by))

if t_min < electrical:
    t = electrical - t_min
    if t % 2 == 1:
        print("N")
    elif t % 2 == 0:
        print("Y")
elif t_min == electrical:
    print("Y")
else:
    print("N")
