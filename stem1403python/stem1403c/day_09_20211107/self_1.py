"""
features of self
reference of the current object
1  the fist parameter
2. access a attribute
3. call instance method
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

    def play(self):
        print("play() is called")

    def live(self):
        self.sleep()
        self.eat()
        self.play()
        # sleep()


# main program
tom = Cat('Tom', 1)
print(tom.name)
print(tom.age)

tom.color = 'Orange'
print(tom.color)

peter = Cat("Peter", 2)
peter.color = "white"
print(peter.color)   # error

tom.live()
print()
peter.live()