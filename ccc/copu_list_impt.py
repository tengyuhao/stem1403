"""
copying a list
"""


import copy
import datetime


class Foo(object):
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return str(self.val)


def createSrcList(N):
    list_src = []
    for i in range(N):
        list_src.append(Foo(i))
    return list_src


def test_listcopy(list_src):
    # copy()
    start = datetime.datetime.now()
    list_dest = list_src.copy()
    end = datetime.datetime.now()
    print('list.copy()')
    print(f'time escaped: {end-start}\n')
    return list_dest


def test_deepcopy(list_src):
    # copy.deepcopy()
    start = datetime.datetime.now()
    list_dest = copy.deepcopy(list_src)
    end = datetime.datetime.now()
    print('copy.deepcopy()')
    print(f'time escaped: {end-start}\n')
    return list_dest


def test_copycopy(list_src):
    # copy.copy()
    start = datetime.datetime.now()
    list_dest = copy.copy(list_src)
    end = datetime.datetime.now()
    print('copy.copy()')
    print(f'time escaped: {end-start}\n')
    return list_dest


def test_list(list_src):
    # list()
    start = datetime.datetime.now()
    list_dest = list(list_src)
    end = datetime.datetime.now()
    print('list()')
    print(f'time escaped: {end-start}\n')
    return list_dest


def test_slice(list_src):
    # list[:]
    start = datetime.datetime.now()
    list_dest = list_src[:]
    end = datetime.datetime.now()
    print('list[:]')
    print(f'time escaped: {end-start}\n')
    return list_dest


# main program
recordNum = 1000000
list_src = createSrcList(recordNum)

test_slice(list_src)
test_copycopy(list_src)
test_listcopy(list_src)
test_list(list_src)
# test_deepcopy(list_src)


