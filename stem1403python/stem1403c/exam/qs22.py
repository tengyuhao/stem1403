class Cat:
    def __init__(self, name="Peter"):
        self.name = name
        self.age = 1

    def __str__(self):
        return f"Cat [name={self.name}, age={self.age}]"


# cat1 = Cat()

print(Cat())
