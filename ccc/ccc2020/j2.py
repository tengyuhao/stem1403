"""
R

input :
P
n
r

Resources: 2.295s, 9.29 MB
Maximum runtime on single test case: 1.896s
Final score: 15/15 (3.0/3 points)
use 15 minute
"""

P = int(input())
N = int(input())
R = int(input())

res = N
res2 = N
day = 1
while True:
    res = res * R
    res2 = res2 + res
    if res2 > P:

        print(day)
        break

    # print(res)
    day += 1
# print(res2)
# print(res)
