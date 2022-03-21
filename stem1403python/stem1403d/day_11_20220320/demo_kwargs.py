"""
*kwagrs
"""

def test(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}

# test(**kwargs)

# test(arg3=3, arg2=2, arg1=1)


# test(2, 1, 3)



def test(**kwargs):
    for items in kwargs:
        print(items, "=", kwargs[items])


kwargs = {"arg3": 30, "arg2": 20, "arg1": 10}
test(**kwargs)