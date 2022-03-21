"""
Case 3:
Accessing methods of parent class

"""


class Parent:
    def __init__(self, name):
        self.name = name + ' parent'

    def draw(self):
        print("parents draws")


class Child(Parent):
    def mydraw(self):
        super().draw()


# test
child1 = Child("Peter")
child1.mydraw()
