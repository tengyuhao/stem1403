"""
Case 2:
Overriding properties and methods of parent class
"""


class Parent:
    def __init__(self, name):
        self.name = name + ' at parent'

    def talk(self):
        print("parents talks")


# child class want to use itself
class Child(Parent):
    # def __init__(self, name):
    #     # super(Child, self).__init__(Child)
    #     self.name = name + ' at child'

    def talk(self):
        print("child talks")


# test
child1 = Child("Peter")
print(child1.name)

child1.talk()
