"""
MultiLevel inherit

"""


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def sleep(self):
        print("sleep")

    def run(self):
        print('run')


class Dog(Animal):
    def bark(self):
        print("Barks.")


class PoliceDog(Dog):
    def fight(self):
        print("Fight with bad guys")

    def sniff(self):
        print("sniff out dangerous product")

    def sleep(self):
        print("sleep")

