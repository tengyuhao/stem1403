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

    # def draw(self):
    #     pass


class Rectangle(Shapes2D):
    def __init__(self, L, l):
        self.name = "Rectangle"
        self.l = l
        self.L = L
        # super.__init__(self.perimeter)

    def getPerimeter(self):
        self.perimeter = 2 * (self.l + self.L)
        return self.perimeter

    def getArea(self):
        self.area = self.l * self.L
        return self.area


class Square(Shapes2D):
    def __init__(self, l):
        self.name = "Square"
        self.l = l
        # super.__init__(self.perimeter, self.area)

    def getPerimeter(self):
        self.perimeter = self.l * 4
        return self.perimeter

    def getArea(self):
        self.area = self.l * self. l
        return self.area


class Circle(Shapes2D):
    def __init__(self, r):
        self.name = "Circle"
        self.r = r
        # super.__init__(self.perimeter, self.area)

    def getPerimeter(self):
        self.perimeter = self.r * 2 * pi
        # print(self.perimeter)
        return self.perimeter

    def getArea(self):
        self.area = self.r * self.r * pi
        # print(self.area)
        return self.area


class Triangle(Shapes2D):
    def __init__(self, a):
        self.name = "Equilateral Triangle"
        self.a = a
        # super.__init__(self.perimeter, self.area)

    def getPerimeter(self):
        self.perimeter = self.a * 3
        # print(self.perimeter)
        return self.perimeter

    def getArea(self):
        self.area = sqrt(3/4 * self.a * self.a)
        # print(self.area)
        return self.area

"""
Project
Starter Edition 3d Part
"""


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
        # super.__init__(self.volume, self.sur_area)

    def getVolume(self):
        self.volume = 4/3 * pi * self.r * self.r * self.r
        return self.volume

    def getSurfaceArea(self):
        self.sur_area = 4 * pi * self.r * self.r
        return self.sur_area


class Cube(Shapes3D):
    def __init__(self, s):
        self.name = "Sphere"
        self.s = s
        # super.__init__(self.volume, self.sur_area)

    def getVolume(self):
        self.volume = self.s * self.s * self.s
        return self.volume

    def getSurfaceArea(self):
        self.sur_area = self.s * self.s * 6
        return self.sur_area
