"""
user-defined exception

keyword: class

step1. define

step2. use
"""

class TooSmallNumberError(Exception):
    pass

class TooBigNumberError(Exception):
    pass

try:
    print("Enter a number between 1 and 100: ", end="")
    num = int(input())

    if num < 1:
        raise TooSmallNumberError("Number is too small")

    if num > 100:
        raise TooBigNumberError("Number is too big")

except TooSmallNumberError as ue1:
    print(ue1)
except TooBigNumberError as ue2:
    print(ue2)
except Exception as e:
    print(e)

finally:
    print("done.")

