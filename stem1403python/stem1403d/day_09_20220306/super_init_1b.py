"""

"""


class Parent:
    def __init__(self, name):
        print("Parent __init__() called")
        self.name = name


class Child(Parent):
    pass


c1 = Child("Peter")
