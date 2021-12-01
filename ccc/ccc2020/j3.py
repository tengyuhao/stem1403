"""
N = number input
cord = x, y = string
cord.split()
listx = x.append()
listy = y.append()

# comparison listx
# comparison listy

max_number_x = -1
for i in listx:
    if i > max_number:
        max_number_x = x

max_number_y = -1
for i in listy:
    if i > max_number_y:
        max_number_y = x


min_number_x = 1000
for i in listx:
    if i < min_number_x:
        max_number_x = x

min_number_y = 1000
for i in listy:
    if i < min_number_y:
        max_number_y = x


max(x) + 1 = right.x
min(x) - 1 = left.x
max(y) +1 = right.y
min(y) -1 = left.y

output
left.x,left.y
right.x,right.y


test
44,62
34,69
24,78
42,44
64,10


Resources: 0.406s, 9.38 MB
Maximum runtime on single test case: 0.026s
Final score: 15/15 (3.0/3 points)
"""

n = int(input())
listx = []
listy = []
for i in range(n):
    cord = input()
    x, y = cord.split(",")
    # print(cord.split(","))
    listx.append(x)
    listy.append(y)

# print(listx)
# print(listy)

max_number_x = -1
for i in listx:
    i = int(i)
    if int(i) > max_number_x:
        max_number_x = i

max_number_y = -1
for i in listy:
    i = int(i)
    if int(i) > max_number_y:
        max_number_y = i


min_number_x = 1000
for i in listx:
    i = int(i)
    if int(i) < min_number_x:
        min_number_x = i

min_number_y = 1000
for i in listy:
    i = int(i)
    if int(i) < min_number_y:
        min_number_y = i

# print(max_number_x)
# print(max_number_y)
# print(min_number_x)
# print(min_number_y)
# print()

"""
max(x) + 1 = right.x
min(x) - 1 = left.x
max(y) +1 = right.y
min(y) -1 = left.y
"""

print(f"{min_number_x-1},{min_number_y-1}")


# res_right = max_number_x+1, max_number_y+1
print(f"{max_number_x+1},{max_number_y+1}")