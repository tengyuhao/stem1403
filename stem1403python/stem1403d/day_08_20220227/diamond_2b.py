"""
Diamond Problem 2B
"""
class A:
    def m(self):
        print("m of A called")


class B(A):
    def m(self):
        print("m of B called")
        super().m()


class C(A):
    def m(self):
        print("m of C called")
        super().m()


class D(B, C):
    def m(self):
        print("m of D called")
        super().m()


print(D.__mro__)

d1 = D()
d1.m()