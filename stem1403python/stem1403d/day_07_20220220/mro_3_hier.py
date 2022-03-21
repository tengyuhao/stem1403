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


class C(A):
    def m(self):
        print("C.m()")


# test
print(B.__mro__)
print(C.__mro__)

# c1 = Child()
# c1.m()