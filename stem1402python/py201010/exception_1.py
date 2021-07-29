
"""
Concept
Error, Exception
Source (Path, file/module, line, code)
Error Type, Error Message (description)
Type of Errors:
1. Syntax Error
2. Logical Error (exception)
    Clear and make sure the goals and expected result
    business rules
    logical algorithm
Error
1. pre-defined error
2. user-defined error
before execution
runtime
What happens when an Error occurs?
exit code 0
a. error occurs
b. user interrupts

"""


# 1. Syntax Error
while True:
    print("aaa")
print("start")
b = 1
print(b)
print("111111")
print("111111")
print("111111")
print("end")
a = 4

if a < 5:
   print("aaaa")
   print("bbbb")


def foo():
    pass


def foo1():
    # dkjasdfd
    pass


if True:
    pass
else:
    #asldfasdf
    pass

print()

# 2. Logical Error (Exception)
a = 8
if a > 0:
    print("Negative")
else:
    print("Positive")
score = 100

# score >=90  A
if score >= 95:
    print("A")

