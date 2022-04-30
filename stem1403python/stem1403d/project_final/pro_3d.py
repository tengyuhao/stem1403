"""
Project
Pro Edition 3d Part
"""

from starter_3d import *


class Shapes3D:
    def __init__(self, color):
        self.name = ""
        self.volume = None
        self.sur_area = None
        self.formulaV = ""
        self.formulaA = ""
        self.color = ""

    def getVolume(self):
        self.volume = self.formulaV
        print(self.volume)

    def getSurfaceArea(self):
        self.sur_area = self.formulaA
        print(self.sur_area)

    def setColor(self, color):
        self.color = color

    def draw(self):
        print(self.name, f"is drawing who has {self.color} color")


class Pyramid(Shapes3D):
    def __init__(self, b, h):
        self.name = "Pyramid"
        self.formulaV = (1/3) * b * h
        self.formulaA = b * 4 * h + b * b


class Cylinder(Shapes3D):
    def __init__(self, r, h):
        self.name = "Cylinder"
        self.formulaV = pi * r * 2 * h
        self.formulaA = 2 * pi * r * r + h * r * 2 * pi

