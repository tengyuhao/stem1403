"""
scope
"""

# using global variable in local scope


def foo():
    global x
    x = 10
    print("local x", x)


x = 5
foo()
print("global x", x)
