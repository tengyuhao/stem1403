"""
Case 4:
Forcely accessing private properties and methods of parent class

super()
self - the reference to the instance of itself
super - the reference to the instance of its parent class
"""


class Parent:
    def __init__(self, name):
        self.name = name + ' at parent'

    def __talk(self):
        print("parents talks")


# child class want to use itself
class Child(Parent):
    def mytalk(self):
        # Not recommended
        super()._Parent__talk()


# test
child1 = Child("Peter")
child1.mytalk()
