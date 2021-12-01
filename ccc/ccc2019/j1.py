"""
资源： 0.354s, 9.35 MB
最慢一次测试的运行时间 0.025s
最终得分： 15/15 (3.0/3 points)
5min
"""

# team Ananas
A3 = int(input())
A2 = int(input())
A1 = int(input())

resA = A3 * 3 + A2 * 2 + A1 * 1
# team bananes
B3 = int(input())
B2 = int(input())
B1 = int(input())
resB = B3 * 3 + B2 * 2 + B1 * 1

if resA > resB:
    print("A")
elif resA < resB:
    print("B")
else:
    print("T")
