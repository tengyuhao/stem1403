"""
recursive function

Recursion is the process of defining something in terms of itself
"""


def summation(n):
    if n < 0:
        return "error"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + summation(n - 1)


n = 100
print(f"The summary of {n} is {summation(n)}")

