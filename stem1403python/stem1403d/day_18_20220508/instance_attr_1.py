"""
instance attribute
"""

class Foo:
    def __init__(self, myname):\
        self.name = myname


foo1 = Foo('Name1')
print(foo1.name)

foo2 = Foo('Name2')
print(foo2.name)

# AttributeError: 'Foo' object has no attribute 'age'
# print(foo1.age)


foo1.age = 16
print(foo1.age)

print(foo1.age + 1)

if foo1.age < 18:
    print("Do not drink alcohol.")
