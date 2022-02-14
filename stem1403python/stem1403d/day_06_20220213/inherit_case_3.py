"""
Case 3:
Accessing methods of parent class

super()
self - the reference to the instance of itself
super - the reference to the instance of its parent class
"""


class Parent:
    def __init__(self, name):
        self.name = name + ' at parent'

    def talk(self):
        print("parents talks")


# child class want to use itself
class Child(Parent):
    def mytalk(self):
        super().talk()

    def talk(self):
        super().talk()

# test
child1 = Child("Peter")
child1.mytalk()
