"""
class member: class method'

cls refer to the Class itself
self refers to the current instance of the class

wor
"""


class Foo:

    # class attribute
    count = 0

    @classmethod
    def get_count(cls):
        # cls.count => Foo.count
        return cls.count

    @classmethod
    def set_count(cls, new_count):
        cls.count = new_count


# test class method
print(Foo.get_count())

Foo.set_count(11)
print(Foo.get_count())\

Foo.set_count(Foo.get_count()+1)
print(Foo.get_count())

