"""
yield
"""

def f1():

    num = 0
    while True:
        num += 1

        if num > 0:
            break

        yield num

# main
print(f1())