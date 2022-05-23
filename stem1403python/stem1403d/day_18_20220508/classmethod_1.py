"""
class member: class method'

cls refer to the Class itself
self refers to the current instance of the class
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

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


# test
foo1 = Foo("NyName1")


# read the instance attribute: name
print(foo1.get_name())

# write the instance attribute: name
foo1.set_name("MyNewName")


# test class method
print(Foo.get_count())
Foo.set_count(11)

print(Foo.get_count()+1)
Foo.set_count(11)


