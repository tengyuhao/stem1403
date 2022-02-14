"""

"""


class Parent:
    def have(self):
        print("parent have baby.")


class Child1(Parent):
    def have(self):
        super().have()
        print("child 1 have parent.")


class Child2(Parent):
    def have(self):
        print("child 2 have baby.")