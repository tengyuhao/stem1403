"""
Module: OOP
Polymorphism

show pet's name
"""


class Pet:
    def __init__(self, petClass='unknown pet'):
        self.petClass = petClass

    def eat(self):
        print("A pet eats food.")


class Cat(Pet):
    def eat(self):
        print("Cat eats fish.")


class Dog(Pet):
    def eat(self):
        print("Dog eats meat.")


class Person:
    def __init__(self, name, mypets=[]):
        self.name = name
        self.mypets = mypets

    def feed(self, pet):
        print(f"{self.name} feeds his {pet.petClass}.")
        pet.eat()
        # print(type(pet))

    def adopt(self, pet):
        print(f"{self.name} just adopted a {pet.petClass}.")
        self.mypets.append(pet)

    def getPets(self):
        # print(self.mypets)
        return self.mypets


# main
def showMyPets(petList):
    for p in petList:
        print(p.petClass)


p1 = Cat("cat")
p2 = Dog("dog")
p3 = Pet()
p4 = Cat("cat")
p5 = Dog("dog")
p6 = Pet()
mypets = [p1, p2, p3, p4, p5, p6]

peter = Person("Peter", mypets)

# jack = Person("Jack")

# before
showMyPets(peter.getPets())
for pi in peter.mypets:
    # Peter feeds his pet
    peter.feed(pi)
    print()

print("============")
# after
p7 = Dog("dog")
peter.adopt(p7)
showMyPets(peter.getPets())
peter.feed(p7)


