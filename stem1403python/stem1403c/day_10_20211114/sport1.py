"""

"""


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weigh = weight

    def run(self):
        self.weigh -= 0.5
        print(f"He ran. He has lose 0,5kg, now he has {self.weigh}kg.")

    def eat(self):
        self.weigh += 1
        print(f"He ate. He has gains 1,0kg, now he has {self.weigh}kg.")

    def __str__(self):
        return f"He has {self.weigh}kg"


peter = Person("Peter", 75)

peter.run()

peter.eat()

peter.run()

peter.run()

peter.eat()

peter.run()

peter.run()

print(peter)


