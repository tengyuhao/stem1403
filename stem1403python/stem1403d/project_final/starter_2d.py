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
        self.formulaP = ""
        self.formulaA = ""

    def getPerimeter(self):
        self.perimeter = self.formulaP
        print(self.perimeter)

    def getArea(self):
        self.area = self.formulaA
        print(self.area)

    def draw(self):
        print(self.name, "is drawing.")


class Rectangle(Shapes2D):
    def __init__(self, L, l):
        self.name = "Rectangle"
        self.formulaP = 2 * (l + L)
        self.formulaA = L * l


class Square(Shapes2D):
    def __init__(self, l):
        self.name = "Square"
        self.formulaP = l * 4
        self.formulaA = l * l


class Circle(Shapes2D):
    def __init__(self, r):
        self.name = "Circle"
        self.formulaP = r * 2 * pi
        self.formulaA = r * r * pi


class Triangle(Shapes2D):
    def __init__(self, a):
        self.name = "Equilateral Triangle"
        self.formulaP = a * 3
        self.formulaA = sqrt(3/4 * a * a)

