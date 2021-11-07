"""
output the info of an object

Why __str__()?
1. debugging and check current state of the object

Is it mandatory?
It depends
for the most entities, Recommended adding it to the definition of class
for some controller or high level class
"""


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 4
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

    def __repr__(self):
        # return self.name+","+str(self.age)
        return f"{self.__class__.__name__}[name={self.name}, age={self.age}, weight={self.weight}]"


# main program
tom = Cat('Tom', 1)
print(tom)
# output: <__main__.Cat object at 0x7f86741befd0>


