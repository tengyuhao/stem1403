"""


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


#  creating multiple objects
peter = Cat('Peter', 1)
jerry = Cat('Jerry', 1)

tom = Cat('Tom', 1)
tom2 = Cat('Tom', 1)
tom3 = Cat('Tom', 1)
# not identical objet

print(id(tom))
print(id(tom2))
print(id(tom3))
"""
140537948327312
140537948327888
140537948327216
"""
# ==========
tom2 = tom
print(id(tom))
print(id(tom2))
