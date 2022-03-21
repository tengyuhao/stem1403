"""
Case 2:
Overriding properties and methods of parent class
"""


class Parent:
    def __init__(self, name):
        self.name = name + ' at parent'

    def draw(self):
        print("parents draws")


class Child(Parent):
    def draw(self):
        print("child draws")


# test
child1 = Child("Sophia")
print(child1.name)

child1.draw()
