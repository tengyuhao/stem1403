"""
object identity
accessing instance attribute
"""


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("eat() is called")

    def sleep(self):
        print("sleep() is called")


tom = Cat('Tom', 1)

# name = tom.name
print(tom.name)

# updating attributes
tom.name = "Peter"
print(tom.name)

# after a year
tom.age = tom.age + 1
print(tom.age)
