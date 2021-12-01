"""
2017 j1
Resources:： 0.378s, 9.35 MB
Maximum runtime on single test case:  0.025s
Final scores : 15/15 (3.0/3 points)
5 minutes used
"""
x = int(input())
y = int(input())

if x > 1 and y >= 0:
    print(1)
elif x<0 and y >= 0:
    print(2)
elif x<0 and y<0:
    print(3)
elif x>0 and y<0:
    print(4)