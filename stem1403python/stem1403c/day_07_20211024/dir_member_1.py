"""
list mermbers (attributes and methods)

dir()

"""

# mylist = [1, 2, 3]
#
# results = dir(mylist)
#
# for i in results:
#     print


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("eat() is called")

    def sleep(self):
        print("sleep() is called")

print(dir(Cat))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'eat', 'sleep']

tom = Cat('Tom', 1)
print(dir(tom))
"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
'age', 'eat', 'name', 'sleep']

"""