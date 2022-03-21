"""

"""


class Parent:
    def __init__(self):
        print("Parent __init__() called")


class Child(Parent):
    def __init__(self, age):
        print("Child __init__() called")
        self.age = age


c1 = Child(16)
