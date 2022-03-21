"""
Notes
"""


class ParentA:
    def m(self):
        print("A.m()")


class ParentB:
    def m(self):
        print("B.m()")


class Child(ParentA, ParentB):
    pass


child1 = Child()
child1.m()