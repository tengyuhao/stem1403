"""
find symmetric point/item in a linear literature
"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def Symmetric(thelist, index):
    # reslen =
    ans = len(thelist) - 1
    res = thelist[ans - index]
    return res

index = 3
Symmetric(list1, index)

print(Symmetric(list1, index))


def symmetric2(thelist, item):
    # reslen =
    # thelist.index(item)
    ans = len(thelist) - 1
    res = thelist[ans - thelist.index(item)]
    return res

item = 3
# symmetric2(list1, item)

print(symmetric2(list1, item))