"""
single inheritance
"""


class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Animal eats.")

class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog1 = Dog("Dog")
dog1.eat()


cat1 = Cat("Cat")
cat1.eat()
