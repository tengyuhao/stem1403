"""
list methods

index(self, object, start stop) - returns the index of the first atched item

"""

mylist = ['this', 'is', 'my', 'favourite', 'music', 'isn\'t', 'it']
mylist = [1, 2, 3, 44, 5, 6, 44, 7, 8]
obj = 44

if obj in mylist:
    i = mylist.index(obj)
    print(f"item found at {i}")
else:
    print("no such item")

start = 4
if obj in mylist[start:]:
    i = mylist.index(obj, start)
    print(f"item found at {i}")
else:
    print("no such item")

start = 4
stop = 6
if obj in mylist[start:stop]:
    i = mylist.index(obj, start, stop)
    print(f"item found at {i}")
else:
    print("no such item")



