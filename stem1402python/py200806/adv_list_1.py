"""
advanced datatypes

list

"""

# creation
# create an emply list
mylist1 = []

# create a normal list
mylist1 = [1, 2, 3]

# create a nested list
mylist1 = [1, ['a', 'b', 'c'], 3]

# create a matrix
matrix = [[1, 2],
           [3, 4]]

# accessing items or element
# index
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# LTR, positive index
print(mylist[3])

# RTL, negative index
print(mylist[-6])

# first item and last item
print(mylist[0])
print(mylist[-1])
print(mylist[len(mylist)-1])
print(mylist[8])

# accessing items in nested list or matrix
mylist1 = [1, ['a', 'b', 'c'], 3]
print(mylist1[1][0])
print(mylist1[1], type(mylist1[1]))

# traversal
for i in mylist:
    print(i, end="\t")
print("\n")

for i in mylist1:
    print(i)
    if isinstance(i, list):
        for j in i:
            print(j, end="\t")
        print()
print("\n")

for row in matrix:
    # print(row, type(row))
    for col in row:
        print(col, end="\t")
    print()



