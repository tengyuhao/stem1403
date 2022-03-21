"""
[Homework]
Date: 2022-02-20
Due date: 2022-02-26
1. Programming practice
Write a utility program in Java for calculating area of shapes.
Shapes are as follows:
(a) circle
(b) square
(c) equilateral triangle
Hints:
Design a parent class such as Shape
Design a method (i.e. method name could be getArea ) to calculate the area in the Shape class
Design classes for every shape
Design a method for each to calculate the area
Those methods must override the method (i.e. getArea )
Those methods have the same signature
Each method accepts one parameter of double type
Be noted that the formula can be taken as a function of x, where x is the parameter as input.
Formulas:
The area of circle:        f(r) = Pi * r * r   (where r is radius as input)
The area of square:        f(a) = a * a    (where a is side of square as input)
The area of equilateral triangle:   Heron's formula (refer to the link below)
References:
https://www.mathsisfun.com/algebra/trig-area-triangle-without-right-angle.html
https://www.mathsisfun.com/geometry/herons-formula.html
"""

import math


class Shapes:
    def getArea(self, a):
        pass


class Circle(Shapes):
    def getArea(self, a):
        return math.pi * a * a


class Square(Shapes):
    def getArea(self, a):
        return a * a


class EquilateralTriangle(Shapes):
    def getArea(self, a):
        s = a * 3
        s = s / 2
        res = s*(s-a)*(s-a)*(s-a)
        return math.sqrt(res)


# main
# test get area of a circle which has a radian of 1
print("Calculate area of shape")


print("""(1) circle
(2) square
(3) equilateral triangle""")
print("The input format must be a integer. 1, 2 or 3")
num = int(input("Please choose the shape you want to calculate :"))
if num == 1:
    r = float(input("Please input the radius of the circle :"))
    c1 = Circle()
    print(round(c1.getArea(r), 4))

elif num == 2:
    s = float(input("Please input the side of the square :"))
    s1 = Square()
    print(round(s1.getArea(s), 4))

elif num == 3:
    s = float(input("Please input the side of the equilateral triangle :"))
    e1 = EquilateralTriangle()
    print(round(e1.getArea(s), 4))

else:
    print("Some error was happening. Please try again later. ")





