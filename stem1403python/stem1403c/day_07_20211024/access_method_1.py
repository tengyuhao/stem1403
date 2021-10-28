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
name = tom.name
print(name)
print(tom.name)

tom.eat()
tom.sleep()
