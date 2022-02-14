"""
Case 4:
defining __init__ method in child class

super()
self - the reference to the instance of itself
super - the reference to the instance of its parent class
"""


class Parent:
    def __init__(self, name):
        self.name = name + ' at parent'
        self.hobby = 'parent hobby'


# child class want to use itself
class Child(Parent):
    def __init__(self, name):
        self.name = name + ' at child'
        self.age = 10
# test
child1 = Child("Peter")
print(child1.name)
# AttributeError: 'Child' object has no attribute 'hobby'
# print(child1.hobby)

print(child1.age)