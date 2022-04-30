"""
Polymorphism
project: my pets
version: v1
"""


class Pet:
    def __init__(self, petClassName):
        self.petClassName = petClassName

    def eat(self):
        print("A pet eats.")


class Cat(Pet):
    def eat(self):
        print("A cat eats")


class Dog(Pet):
    def eat(self):
        print("A dog eats")



class Person:
    def __init__(self, name):
        self.name = name

    def feed(self, mypet):
        print(f"{self.name} feeds his/her {mypet.petClassName}.")
        mypet.eat()


# main
# Peter feeds his/her pets everyday

person1 = Person("Peter")
print(person1)
print(person1.name)

cat1 = Cat("cat")
person1.feed(cat1)

dog1 = Dog("dog")
person1.feed(dog1)
