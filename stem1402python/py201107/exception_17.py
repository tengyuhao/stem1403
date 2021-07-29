"""
user-defined exception

keyword: class

step1. define

step2. use

step3. import
"""

import py201107.myerrors as err
from py201107.myerrors import *

try:
    print("Enter a number between 1 and 100: ", end="")
    num = int(input())

    if num < 1:
        raise err.TooSmallNumberError("Number is too small")

    if num > 100:
        raise err.TooBigNumberError("Number is too big")

except err.TooSmallNumberError as ue1:
    print(ue1)
except err.TooBigNumberError as ue2:
    print(ue2)
except Exception as e:
    print(e)

finally:
    print("done.")

