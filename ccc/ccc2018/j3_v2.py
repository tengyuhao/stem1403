"""
2018 J3
资源： 0.103s, 9.47 MB
最慢一次测试的运行时间 0.026s
最终得分： 15/15 (3.0/3 points)
"""
distance = input()
distance = distance.split(" ")

for i in range(len(distance)):
    distance[i] = int(distance[i])
# distance = [3, 10, 12, 5]
line1 = f"{0} {distance[0]} {distance[1] + distance[0]} {distance[1] + distance[0] + distance[2]} {distance[1] + distance[0] + distance[2]+distance[3]}"
line2 = f"{distance[0]} {0} {distance[1]} {distance[2] + distance[1]} {distance[2] + distance[1]+distance[3]}"
line3 = f"{distance[0] + distance[1]} {distance[1]} {0} {distance[2]} {distance[3] + distance[2]}"
line4 = f"{distance[1] + distance[0] + distance[2]} {distance[2] + distance[1]} {distance[2]} {0} {distance[3]}"
line5 = f"{distance[1] + distance[0] + distance[2]+distance[3]} {distance[2] + distance[1]+distance[3]} {distance[3] + distance[2]} {distance[3]} {0}"
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
