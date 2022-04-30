"""
Project
Starter Edition 3d Part
"""

from math import pi


class Shapes3D:
    def __init__(self):
        self.name = ""
        self.volume = None
        self.sur_area = None
        self.formulaV = ""
        self.formulaA = ""

    def getVolume(self):
        self.volume = self.formulaV
        print(self.volume)

    def getSurfaceArea(self):
        self.sur_area = self.formulaA
        print(self.sur_area)

    def draw(self):
        print(self.name, "is drawing.")


class Sphere(Shapes3D):
    def __init__(self, r):
        self.name = "Sphere"
        self.formulaV = 4/3 * pi * r * r * r
        self.formulaA = 4 * pi * r * r


class Cube(Shapes3D):
    def __init__(self, s):
        self.name = "Sphere"
        self.formulaV = s * s * s
        self.formulaA = s * s * 6
