"""

"""


class Parent:
    def __init__(self, name):
        print("Parent __init__() called")
        self.name = name


class Child(Parent):
    def __init__(self, age, name):
        print("Child __init__() called")
        self.age = age
        super().__init__(name)


c1 = Child('Peter', 16)
print(c1.age)
print(c1.name)

