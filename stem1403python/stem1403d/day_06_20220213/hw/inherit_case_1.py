"""
Case 1
"""


class Parent:
    def __init__(self, name):
        self.name = name

    def draw(self):
        print("draws")


class Child(Parent):
    pass


# test
child1 = Child("Alice")
print(child1.name)

child1.draw()
