"""
advantage inheritance
"""


class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Animal eats.")

    def drink(self):
        print("Animal drinks.")

class Dog():

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Animal eats.")

    def drink(self):
        print("Animal drinks.")


class Cat():

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Animal eats.")

    def drink(self):
        print("Animal drinks.")


# Must write by yourself if not inheritance
dog1 = Dog("Dog")
dog1.eat()


cat1 = Cat("Cat")
cat1.eat()
