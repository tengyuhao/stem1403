"""
Resources: 0.401s, 9.36 MB
Maximum runtime on single test case: 0.025s
Final score: 15/15 (3.0/3 points)
J3 rewrite
Test value :
44,62
34,69
24,78
42,44
64,10

"""
max_number_x = -1
min_number_x = 100
max_number_y = -1
min_number_y = 100

n = int(input())

for i in range(n):
    cord = input()
    x, y = cord.split(",")
    x = int(x)
    y = int(y)
    if x > max_number_x:
        max_number_x = x
    if x < min_number_x:
        min_number_x = x
    if y > max_number_y:
        max_number_y = y
    if y < min_number_y:
        min_number_y = y

# print(max_number_x, max_number_y, min_number_x, min_number_y)

print(f"{min_number_x-1},{min_number_y-1}")


# res_right = max_number_x+1, max_number_y+1
print(f"{max_number_x+1},{max_number_y+1}")