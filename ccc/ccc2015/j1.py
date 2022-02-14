"""
2015 J1
资源： 0.167s, 9.43 MB 
最慢一次测试的运行时间 0.023s 
最终得分： 15/15 (3.0/3 points) 
"""

month = int(input())
day = int(input())


if month <= 2 and day < 18:
    print("Before")
elif month == 1:
    print("Before")
elif month == 2 and day == 18:
    print("Special")
elif month == 2 and day > 18:
    print("After")
elif month > 2:
    print("After")
