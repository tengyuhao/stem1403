"""
lambda map()
"""

# original list
mylist = [1, 2, 3, 4, 5, 6, 7]

# generate a new list based on the original one
# new item = square of item (item ** 2)
a = map(lambda x: x**2, mylist)
print(a, type(a))

# extract data from map
b = list(a)
print(b, type(b))


# ex - 1
# generate a new list based on the given one using map() and lambda
dataset = ['a', 'b', 'c']

# expected
# newdataset = [97, 98, 99]
c = map(lambda x: ord(x), dataset)
d = list(c)

# extract data from map
print(d, type(d))
