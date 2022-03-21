"""
mro 1
single
"""


class A:
    def m(self):
        print("A.m()")


class B:
    def m(self):
        print("B.m()")


class C(A, B):
    def m(self):
        print("C.m()")


class C2(B, A):
    def m(self):
        print("C2.m()")


# test
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(C2.__mro__)
# (<class '__main__.C2'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
