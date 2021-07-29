"""
remove items from a list

1. del (keyword)

"""

mylist = [1, 2, 3, 4, 5, 6, 7, 8]

# del one item
del mylist[3]
print(mylist)

# del multi items (slicing)
del mylist[0:2]
print(mylist)

# del entire list
del mylist      # NameError
# print(mylist)

# del all items
mylist = [1, 2, 3, 4, 5, 6, 7, 8]
del mylist[:]
print(mylist)
