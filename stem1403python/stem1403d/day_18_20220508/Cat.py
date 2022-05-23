"""
Demo of class method
"""


class Cat:
    species = "Orange"

    @classmethod
    def get_name(cls):
        return cls.species


# test
print(Cat.get_name())