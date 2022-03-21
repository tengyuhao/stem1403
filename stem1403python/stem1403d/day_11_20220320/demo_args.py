"""
* args
"""


# define a function
def foo(*args):
    for i in args:
        print(i)


# test
foo(1, 'aaa', 'bbb', 'ccc')

# foo()
# print(end='')
