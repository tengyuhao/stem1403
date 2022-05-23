"""
Project
Pro Edition 2d Part
"""

from starter_2d import *


class Shapes2D:
    def __init__(self):
        self.name = ""
        self.perimeter = None
        self.area = None
        self.color = ""

    def getPerimeter(self):
        pass

    def getArea(self):
        pass

    def setColor(self, color):
        self.color = color

    def draw(self):
        print(self.name, f"is drawing who has {self.color} color")


class Parallelogram(Shapes2D):
    def __init__(self, a, b, h):
        self.name = "Parallelogram"
        self.a, self.b, self.h = a, b, h
        self.formulaA = h * b
        super.__init__(self.perimeter, self.area)

    def getPerimeter(self):
        self.perimeter = 2 * (self.a + self.b)
        print(self.perimeter)

    def getArea(self):
        self.area = self.h * self.b
        print(self.area)


class Oval(Shapes2D):
    def __init__(self, a, b):
        self.name = "Oval"
        self.a, self.b = a, b
        super.__init__(self.perimeter, self.area)

    def getPerimeter(self):
        self.perimeter = 2 * pi * self.b + 4 * (self.a - self.b)
        print(self.perimeter)

    def getArea(self):
        self.area = self.a * self.b * pi
        print(self.area)


class Rhombus(Shapes2D):
    def __init__(self, a, c, d):
        self.name = "Rhombus"
        self.a, self.c, self.d = a, c, d
        super.__init__(self.perimeter, self.area)

    def getPerimeter(self):
        self.perimeter = self.a * 4
        print(self.perimeter)

    def getArea(self):
        self.area = self.c * self.d / 2
        print(self.area)


class TriangleR(Shapes2D):
    def __init__(self, b, h, hy):
        self.name = "Right Triangle"
        self.b, self.h, self.hy = b, h, hy
        super.__init__(self.perimeter, self.area)

    def getPerimeter(self):
        self.perimeter = self.b + self.h + self.hy
        print(self.perimeter)

    def getArea(self):
        self.area = self.b * self.h
        print(self.area)