"""
Case 1:
Directly accessing properties and methods of parent class
"""


class Parent:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("talks")


class Child(Parent):
    pass


# test
child1 = Child("Peter")
print(child1.name)

child1.talk()
