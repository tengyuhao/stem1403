"""
Notes 
"""


class ParentA:
    # def m(self):
    #     print("A.m()")
    pass


class ParentB:
    def m(self):
        print("B.m()")


class Child(ParentA, ParentB):
    # def m(self):
    #     print("C.m()")
    pass


child1 = Child()
child1.m()
