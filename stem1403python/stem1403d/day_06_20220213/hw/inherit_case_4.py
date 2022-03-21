"""
Case 4

"""


class Parent:
    def __init__(self, name):
        self.name = name + ' at parent'

    def __draw(self):
        print("parents draws")


class Child(Parent):
    def mydraw(self):
        super()._Parent__draw()


# test
child1 = Child("Peter")
child1.mydraw()
