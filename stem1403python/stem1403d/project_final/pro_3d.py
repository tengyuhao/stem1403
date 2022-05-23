"""
Project
Pro Edition 3d Part
"""

from starter_3d import *


class Shapes3D:
    def __init__(self):
        self.name = ""
        self.volume = None
        self.sur_area = None
        self.color = ""

    def getVolume(self):
        pass

    def getSurfaceArea(self):
        pass

    def setColor(self, color):
        self.color = color

    def draw(self):
        print(self.name, f"is drawing who has {self.color} color")


class Pyramid(Shapes3D):
    def __init__(self, b, h):
        self.name = "Pyramid"
        self.b, self.h = b, h
        super.__init__(self.volume, self.sur_area)

    def getVolume(self):
        self.volume = (1/3) * self.b * self.h
        print(self.volume)

    def getSurfaceArea(self):
        self.sur_area = self.b * 4 * self.h + self.b * self.b
        print(self.sur_area)


class Cylinder(Shapes3D):
    def __init__(self, r, h):
        self.name = "Cylinder"
        self.r, self.h = r, h
        super.__init__(self.volume, self.sur_area)

    def getVolume(self):
        self.volume = pi * self.r * 2 * self.h
        print(self.volume)

    def getSurfaceArea(self):
        self.sur_area = 2 * pi * self.r * self.r + self.h * self.r * 2 * pi
        print(self.sur_area)

