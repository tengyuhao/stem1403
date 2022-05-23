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

    def getVolume(self):
        pass

    def getSurfaceArea(self):
        pass

    def draw(self):
        print(self.name, "is drawing.")


class Sphere(Shapes3D):
    def __init__(self, r):
        self.name = "Sphere"
        self.r = r
        super.__init__(self.volume, self.sur_area)

    def getVolume(self):
        self.volume = 4/3 * pi * self.r * self.r * self.r
        print(self.volume)

    def getSurfaceArea(self):
        self.sur_area = 4 * pi * self.r * self.r
        print(self.sur_area)


class Cube(Shapes3D):
    def __init__(self, s):
        self.name = "Sphere"
        self.s = s
        super.__init__(self.volume, self.sur_area)

    def getVolume(self):
        self.volume = self.s * self.s * self.s
        print(self.volume)

    def getSurfaceArea(self):
        self.sur_area = self.s * self.s * 6
        print(self.sur_area)
