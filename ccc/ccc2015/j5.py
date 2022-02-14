"""
2015 J5
资源： 0.223s, 10.29 MB
最慢一次测试的运行时间 0.033s
最终得分： 15/15 (10.0/10 points)
Rewrite for n times
"""

num_pizza = int(input())
people = int(input())
f = [[0 for i in range(people+1)] for i in range(num_pizza+1)]
f[0][1] = 1
print(f)

for i in range(1, num_pizza+1):
    for j in range(1, min(people, i)+1):
        if i == j:
            f[i][j] = 1
        f[i][j] = f[i - 1][j - 1] + f[i - j][j]

print(f[num_pizza][people])
