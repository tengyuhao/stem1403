"""

"""


class GrandParent:
    # not accessed in this case
    def __init__(self, name):
        print('GrandParent __init__() called.')
        self.name = name


class Son(GrandParent):
    # accessed and parameters matched
    def __init__(self, name, age):
        print('Son __init__() called.')
        self.age = age
        super().__init__(name)


class GrandSon(Son):
    def __init__(self, name, age, gender):
        print('GrandSon __init__() called.')
        self.gender = gender
        super().__init__(name, age)


# main
gs1 = GrandSon('Peter', 16, 'M')
print(gs1.name)
print(gs1.age)
print(gs1.gender)









