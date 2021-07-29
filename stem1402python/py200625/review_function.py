"""



"""

# define a function


def foo1():
    print("1111")
    print("1112")
    print("1113")
    print("1114")
    print("1115")
    a = 1
    b = a + 1
    print(b)
    return b


# call a function
print("==== The 1st cal ====")
foo1()
print()

# get the returned value and just use it for only once
print("==== The 2nd cal ====")
print(foo1())
print()

# get the returned value and use it for multiple times
print("==== The 3rd cal ====")
# 1. print out(use) the returned value for the 1st time
result1 = foo1()
print("result", result1)
# 2. use the returned value again
double_result1 = 2 * result1
print("double_result1 = ", double_result1)

# call multiples times
foo1()
foo1()
print(foo1())



