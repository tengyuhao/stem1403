"""
what is the lambda function?
anonymous function

"""

# syntax
# lambda para1, [para2, ...] : expr

# covert a regular function to lambda


def double(n):
    return 2 * n


db1 = lambda n: 2 * n

print(db1(5))

# using filter()
mylist = [1, 2, 3, 4, 5, 6, 7]

# how to pick up all the odd numbers from the list using lambda
print(list(filter(lambda x: x % 2 == 1, mylist)))
print(filter(lambda x: x % 2 == 1, mylist))






