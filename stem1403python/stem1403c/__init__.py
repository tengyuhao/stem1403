class Dog():
    def __init__(self, age, name, color):
        self.age = age
        self.name = name
        self.color = color


dog1 = Dog(2, "Peter", "White")
dog1.name = "Pierre"
dog1.age = 3
dog1.color = "Black"

print(dog1.age, dog1.name, dog1.color)
# 3 Pierre Black
1