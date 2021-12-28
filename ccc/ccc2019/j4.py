"""
2019 j4
资源： 2.303s, 17.68 MB
最慢一次测试的运行时间 0.333s
最终得分： 15/15 (3.0/3 points)
"""
put = input("")
# put.split("")
put = list(put)
matrix = [[1, 2],
          [3, 4]]

for i in put:
    if i == "H":
        matrix = matrix[::-1]
        # print(matrix)
    elif i == "V":
        for i in range(len(matrix)):
            matrix[i].reverse()


# print(matrix)

print(f"{matrix[0][0]} {matrix[0][1]}")
print(f"{matrix[1][0]} {matrix[1][1]}")