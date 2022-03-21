"""
Case 4:
defining __init__ method in child class

"""


class Parent:
    def __init__(self, name):
        self.name = name + ' at parent'
        self.hobby = 'parent hobby hockey'


#
class Child(Parent):
    def __init__(self, name):
        self.name = name + ' at child'
        self.age = 10


# test
child1 = Child("Peter")
print(child1.name)

print(child1.age)