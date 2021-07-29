"""
namespace

is a collection of name (identifiers)

1. built-in namespace
2. module: global namespace
3. function: local namespace
"""


def foo():
    x = 10
    print("1. local x=", x)
    x = "abc"
    print("2. local x=", x)


x = 5
print("1. global x=", x)

foo()

x = 51
print("2. global x=", x)

foo()

