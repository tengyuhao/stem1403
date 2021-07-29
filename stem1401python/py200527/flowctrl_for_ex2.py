"""
print out a matrix

nested if
for

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

"""
matrix = [[1, 2, 3], [4, 5, 6, 10], [7, 8, 9, 55, 66]]

for row in matrix:
    # print(row)
    for col in row:
        print(col, end="\t")

    print()
