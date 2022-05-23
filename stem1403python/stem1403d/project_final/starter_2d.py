"""
Project
Stater Edition 2d Part
"""

from math import pi, sqrt


class Shapes2D:
    def __init__(self):
        self.name = ""
        self.perimeter = None
        self.area = None

    def getPerimeter(self):
        pass

    def getArea(self):
        pass

    def draw(self):
        print(self.name, "is drawing.")


class Rectangle(Shapes2D):
    def __init__(self, L, l):
        self.name = "Rectangle"
        self.l = l
        self.L = L
        super.__init__(self.perimeter, self.area)

    def getPerimeter(self):
        self.perimeter = 2 * (self.l + self.L)
        print(self.perimeter)

    def getArea(self):
        self.area = self.l * self.L
        print(self.area)


class Square(Shapes2D):
    def __init__(self, l):
        self.name = "Square"
        self.l = l
        super.__init__(self.perimeter, self.area)

    def getPerimeter(self):
        self.perimeter = self.l * 4
        print(self.perimeter)

    def getArea(self):
        self.area = self.l * self. l
        print(self.area)


class Circle(Shapes2D):
    def __init__(self, r):
        self.name = "Circle"
        self.r = r
        super.__init__(self.perimeter, self.area)

    def getPerimeter(self):
        self.perimeter = self.r * 2 * pi
        print(self.perimeter)

    def getArea(self):
        self.area = self.r * self.r * pi
        print(self.area)


class Triangle(Shapes2D):
    def __init__(self, a):
        self.name = "Equilateral Triangle"
        self.a = a
        super.__init__(self.perimeter, self.area)

    def getPerimeter(self):
        self.perimeter = self.a * 3
        print(self.perimeter)

    def getArea(self):
        self.area =  sqrt(3/4 * self.a * self.a)
        print(self.area)

