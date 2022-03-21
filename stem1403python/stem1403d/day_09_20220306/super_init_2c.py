"""

"""


class Parent:
    def __init__(self, name):
        print("Parent __init__() called")
        self.name = name


class Child(Parent):
    def __init__(self, age):
        print("Child __init__() called")
        self.age = age


c1 = Child(16)
