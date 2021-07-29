"""
scope 4. nested function
"""


def outer():
    x = "local"

    def inner():
        # pass
        x = "nonlocal"
        print("inner", x)

    inner()
    print("outer: ", x)


outer()
