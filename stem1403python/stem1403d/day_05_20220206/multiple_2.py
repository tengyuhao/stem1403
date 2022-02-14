"""
multiple inherit
ver2
"""


class Father:
    def dance(self):
        print("Parentb dance")


class Mother:
    def sing(self):
        print("A sing")


class Child(Father, Mother):
    pass


class Child2(Mother, Father):
    pass


peter = Child()
peter.sing()
peter.dance()

jack = Child2()
jack.sing()
jack.dance()


