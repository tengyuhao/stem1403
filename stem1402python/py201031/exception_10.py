"""
how to raise an error
input a number
this number should be in range of [1, 100]
"""

"""
< 1, > 100
"""

print("Enter a number between 1 and 100: ", end="")
try:
    num = int(input())

    # if num > 100 or num < 1:
    #     raise ValueError("Out of range")
    if num > 100:
        raise ValueError("Out of range, Too big")
    elif num < 1:
        raise ValueError("Out of range, Too small")

except ValueError as ve:
    print(ve)
except TypeError as te:
    print(te)