"""
mro 5
hybrid
"""


class A:
    # def m(self):
    #     print("A.m()")
    pass


class B(A):
    # def m(self):
    #     print("B.m()")
    pass


class C(A):
    # def m(self):
    #     print("C.m()")
    pass


class D(B, C):
    # def m(self):
    #     print("C2.m()")
    pass


# test
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
