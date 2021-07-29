"""
copy() - return a shallow copy of the list
"""

mylist = [1, 2, 3]
mylist2 = mylist.copy()
print('mylist', mylist)
print('mylist2', mylist2)

print(mylist == mylist2)
print(mylist is mylist2)
print(id(mylist))
print(id(mylist2))
print()

mylist[0] = 11
print(mylist)
print(mylist2)
print()


mylist = [1, 2, 3]
mylist3 = mylist
print(mylist3 == mylist)
print(mylist is mylist3)

mylist[0] = 11
print(mylist3)

