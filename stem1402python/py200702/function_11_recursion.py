"""
recursive function

Recursion is the process of defining something in terms of itself
"""


# factorial
# 1 x 2 x 3 x 4 x 5 x...x n = ?
# 1 x 2 x 3 x 4 x 5 x 6

# step 1.
# result = 1
# n = 10
# for i in range(1, n+1):
#     result *= i
# print(f'result = {result}')


# step 2.
def factorial(n):
    result = None
    if n < 0:
        result = "error"
    elif n == 0:
        result = 1
    elif n == 1:
        result = 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
    return result


print("The result is {}".format(factorial(-1)))
print("The result is {}".format(factorial(0)))
print("The result is {}".format(factorial(1)))
print("The result is {}".format(factorial(2)))
print("The result is {}".format(factorial(6)))




