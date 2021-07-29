"""
global local variable and scope
"""


def foo():
    print(x)


def foo2():
    print(x+str(1))


# def foo3():
#     x = x + str(1)
#     print(x)


foo()
foo2()
# foo3()

x = "global"

