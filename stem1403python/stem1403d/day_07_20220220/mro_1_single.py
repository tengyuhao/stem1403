"""
mro 1
single
"""


class Parent:
    def m(self):
        print("A.m()")


class Child(Parent):
    def m(self):
        print("B.m()")


# test
print(Child.__mro__)
c1 = Child()
c1.m()