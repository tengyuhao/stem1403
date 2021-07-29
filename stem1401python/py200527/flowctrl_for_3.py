"""
scope of local name(variables)
"""

val = 10
print(val)

for val in [1, 2, 3, 4]:
    print(val)


# range()
# range(n)
a = range(10)
print(a, type(a))

# list()
print(list(a))

for i in range(10):
    print(i)

for i in list(range(10)):
    print(i)

# range(1,11)
a = range(1, 11)
print(list(a), type(a))

# range(1,11,2)
a = range(1, 11, 2)
print(list(a), type(a))


