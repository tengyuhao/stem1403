"""
Project
Pro Edition 2d Part + 3d part
"""

from math import pi, sqrt


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

    # def setColor(self, color):
    #     self.color = color

    # def draw(self):
    #     print(self.name, f"is drawing who has {self.color} color")


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


class Parallelogram(Shapes2D):
    def __init__(self, a, b, h):
        self.name = "Parallelogram"
        self.a, self.b, self.h = a, b, h
        # super.__init__(self.perimeter, self.area)

    def getPerimeter(self):
        self.perimeter = 2 * (self.a + self.b)
        return self.perimeter

    def getArea(self):
        self.area = self.h * self.b
        return self.area


class Oval(Shapes2D):
    def __init__(self, a, b):
        self.name = "Oval"
        self.a, self.b = a, b
        # super.__init__(self.perimeter, self.area)

    def getPerimeter(self):
        self.perimeter = 2 * pi * self.b + 4 * (self.a - self.b)
        return self.perimeter

    def getArea(self):
        self.area = self.a * self.b * pi
        return self.area


class Rhombus(Shapes2D):
    def __init__(self, a, c, d):
        self.name = "Rhombus"
        self.a, self.c, self.d = a, c, d
        # super.__init__(self.perimeter, self.area)

    def getPerimeter(self):
        self.perimeter = self.a * 4
        return self.perimeter

    def getArea(self):
        self.area = self.c * self.d * 1/2
        return self.area


class TriangleR(Shapes2D):
    def __init__(self, b, h, hy):
        self.name = "Right Triangle"
        self.b, self.h, self.hy = b, h, hy
        # super.__init__(self.perimeter, self.area)

    def getPerimeter(self):
        self.perimeter = self.b + self.h + self.hy
        return self.perimeter

    def getArea(self):
        self.area = self.b * self.h
        return self.area


"""
Project
Pro Edition 3d Part
"""


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

    # def setColor(self, color):
    #     self.color = color
    #
    # def draw(self):
    #     print(self.name, f"is drawing who has {self.color} color")


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


class Pyramid(Shapes3D):
    def __init__(self, b1, b2, h):
        self.name = "Pyramid"
        self.b, self.h = b1 * b2, h
        self.b1 = b1
        self.b2 = b2
        # super.__init__(self.volume, self.sur_area)

    def getVolume(self):
        self.volume = (1 / 3) * self.b * self.h
        return self.volume

    def getSurfaceArea(self):
        self.sur_area = (1/2 * (self.b1 + self.b2)*2 * self.h) + self.b1 * self.b2
        return self.sur_area


class Cylinder(Shapes3D):
    def __init__(self, r, h):
        self.name = "Cylinder"
        self.r, self.h = r, h
        # super.__init__(self.volume, self.sur_area)

    def getVolume(self):
        self.volume = pi * self.r * 2 * self.h
        return self.volume

    def getSurfaceArea(self):
        self.sur_area = 2 * pi * self.r * self.r + self.h * self.r * 2 * pi
        return self.sur_area
