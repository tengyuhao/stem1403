def foo(mlist):
    mlist[0] = 9
    print(mlist)


mylist = [1,2,3]
print(mylist)
foo(mylist)
print(mylist)
mylist[0] = 99
print(mylist)