"""

"""


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weigh = weight

    def run(self):
        self.weigh -= 0.5
        return f"{self.name} ran. {self.name} has lose 0,5kg, now {self.name} has {self.weigh}kg."

    def eat(self):
        self.weigh += 1
        return f"{self.name} ate. {self.name} has gains 1,0kg, now {self.name} has {self.weigh}kg."

    def __str__(self):
        return f"{self.name} has {self.weigh}kg"


peter = Person("Peter", 75)
amy = Person('Amy', 45)
peter.run()
amy.run()
peter.eat()
amy.eat()
peter.run()
amy.run()
peter.run()
amy.run()
peter.eat()
amy.eat()
peter.run()
amy.run()
peter.run()
amy.run()
print(peter)
print(amy)

