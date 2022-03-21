N = int(input())
T = int(input())

matrix = [[0 for i in range(N)] for i in range(N)]

for i in range(T):
    info = input()
    x, y = info.split()
    matrix[int(x)-1][int(y)-1] = 1

if T == 1:
    total = int(x) + int(y)



else:
    pass

"""
15
8
4 7
4 1
14 11 
10 6 
13 4 
4 10 
10 3 
9 14
"""
# print(matrix)




