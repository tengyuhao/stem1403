"""
Case 5:
defining __init__ method in child class

super()
self - the reference to the instance of itself
super - the reference to the instance of its parent class
"""


class Parent:
    def __init__(self, name, work):
        self.name = name + " parent's name "
        self.work = 'hard' + work


# child class want to use itself
class Child(Parent):
    def __init__(self, name, work):
        # self.name = name + " child's name "
        self.age = 12
        super().__init__(name, work)

# test
child1 = Child("Peter", 'Accountingh')
print(child1.name)
print(child1.age)
print(child1.work)

parent1 = Parent("Jack", "Painting")
print(parent1.name)
print(parent1.work)

# print(parent1.age)