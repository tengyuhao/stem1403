"""
sort() - sort items in a list in ascending order
"""

mylist = ['It', 'is', 'my', 'favourite', 'music', 'isn\'t', 'it']
a = mylist.sort()
print(a, type(a))
print(mylist)
print()

mylist = ['It', 'is', 'my', 'favourite', 'music', 'isn\'t', 'it', '', ' ', '\t', '\n', ]
a = mylist.sort()
print(mylist)
print()

mylist = ['It', 'is', 'my', 'favourite', 'music', 'isn\'t', 'it', '', ' ', '\t', '\n', ]
a = mylist.sort(reverse=True)
print(mylist)
print()

