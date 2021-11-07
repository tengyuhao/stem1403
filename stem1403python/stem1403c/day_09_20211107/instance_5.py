"""
adding temperate attribute to an object/instance


"""


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.color = None

    def eat(self):
        print("eat() is called")

    def sleep(self):
        print("sleep() is called")


# main program
tom = Cat('Tom', 1)
print(tom.name)
print(tom.age)

tom.color = 'Orange'
print(tom.color)

peter = Cat("Peter", 2)
peter.color = "white"
print(peter.color)   # error
