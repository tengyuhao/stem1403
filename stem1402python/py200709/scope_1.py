"""
Global, Local variables and scope

scope
- the scope of the system
- the scope of variables where they take effect
"""


# ex 1. create a global var
"""
def foo():
    print(f"x inside: {x}")


x = "global"
foo()

print(f"x outide: {x}")
"""


# ex 2. change a global var
def foo():
    print(f"x inside: {x+'2'}")


x = "global"
foo()

print(f"x outide: {x}")


# ex 3. change a global var
def foo():
    # x = x + '2'
    # x = x
    print(f"x inside: {x+'2'}")


x = "global"
foo()

print(f"x outide: {x}")
