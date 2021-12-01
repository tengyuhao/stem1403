"""
资源： 0.378s, 9.36 MB
最慢一次测试的运行时间 0.026s
最终得分： 15/15 (3.0/3 points)
15min
"""

first = int(input())
second = int(input())
third = int(input())
forth = int(input())

if first == 8 or first == 9:

    if forth == 8 or forth == 9:
        # print(1)
        if second == third:
            print("ignore")
        else:
            print("answer")

    else:
        print("answer")

else:
    print("answer")
