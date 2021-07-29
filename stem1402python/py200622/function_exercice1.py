"""
crate 2 functions
1. y = 2x
2. y = 2x + 1
(whereas 2x mean 2 * x)

call each function for 3 time with different input x of x (value of x)
then print out the returned value of y
"""

# define function with the keyword 'def'

# define a function

def func1a(x):
    y = 2 * x
    return y

def func1b(x):
    y = 2 * x + 1
    return y

# 1. y = 2x
# call a function
result = func1a(5)
print("result: for y = 2x when x = 5, then y = {} ".format(result))

# call a function again
result = func1a(10)
print("result: for y = 2x when x = 10, then y = {} ".format(result))

# call a function again
result = func1a(55)
print("result: for y = 2x when x = 55, then y = {} ".format(result))

print()

# 2. y = 2x + 1
# call a function
result = func1b(5)
print("result: for y = 2x + 1 when x = 5, then y = {} ".format(result))

# call a function again
result = func1b(10)
print("result: for y = 2x + 1 when x = 10, then y = {} ".format(result))

# call a function again
result = func1b(55)
print("result: for y = 2x + 1 when x = 55, then y = {} ".format(result))




