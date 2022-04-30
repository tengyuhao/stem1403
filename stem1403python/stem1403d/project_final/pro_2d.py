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
        self.formulaP = ""
        self.formulaA = ""
        self.color = ""

    def getPerimeter(self):
        self.perimeter = self.formulaP
        print(self.perimeter)

    def getArea(self):
        self.area = self.formulaA
        print(self.area)

    def setColor(self, color):
        self.color = color

    def draw(self):
        print(self.name, f"is drawing who has {self.color} color")


class Parallelogram(Shapes2D):
    def __init__(self, a, b, h):
        self.name = "Parallelogram"
        self.formulaP = 2 * (a + b)
        self.formulaA = h * b


class Oval(Shapes2D):
    def __init__(self, a, b):
        self.name = "Oval"
        self.formulaP = 2 * pi * b + 4 * (a - b)
        self.formulaA = a * b * pi


class Rhombus(Shapes2D):
    def __init__(self, a, c, d):
        self.name = "Rhombus"
        self.formulaP = a * 4
        self.formulaA = c * d / 2


class TriangleR(Shapes2D):
    def __init__(self, b, h, hy):
        self.name = "Right Triangle"
        self.formulaP = b + h + hy
        self.formulaA = b * h

