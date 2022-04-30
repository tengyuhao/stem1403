"""
Module: OOP
Polymorphism
version 5
petsys
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


class Hamster(Pet):
    def eat(self):
        print("Hamster eats grain.")


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

