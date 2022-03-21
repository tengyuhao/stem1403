"""
mro 1
single
"""


class A:
    def m(self):
        print("A.m()")


class B(A):
    def m(self):
        print("B.m()")


class C(B):
    # def m(self):
    #     print("C.m()")
    pass


# test
print(C.__mro__)

# c1 = Child()
# c1.m()