"""
initialization problem
"""


class Parent:
    def __init__(self,name):
        self.name = name


class Child(Parent):
    def __init__(self, age, name):
        self.age = age


child1 = Child('Peter', 16)
print(child1.name)
print(child1.age)