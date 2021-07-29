"""
String formatting output
"""


def foo():
    return 1


def foo2(n):
    return n


s = "string template {}".format(1)
print(s)

s2 = f"string template {1}"
print(s2)

n = 1
s2 = f"string template {n}"
print(s2)

s2 = f"string template {foo()}"
print(s2)

s2 = f"string template {foo2(10)}"
print(s2)





