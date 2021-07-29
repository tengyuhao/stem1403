"""

"""

"""
def foo(y):
    print("foo()", y)

x = 10
print(x)

foo(x)
"""

# Local var and global share the same name


def foo():
    x = 10
    print("local x", x)


x = 5
foo()
print("global x", x)
