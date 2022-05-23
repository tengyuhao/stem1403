"""

"""
from starter import *
print("Welcome to Project Potter. Choose that you want to work in 2D Shapes or 3D Shapes")
print("""1) 2D
2) 3D""")
choose1 = input("Please input your choose here : ")


def print_info(name, value, v1_name, v2_name, v3_name, function):
    print(f"\nWelcome to {name} Section Page!")
    print(f"You need {value} values to finish your work;")
    v1 = int(input(f"fPlease input the value for {v1_name} : "))

    if v2_name != None:

        v2 = int(input(f"Please input the value for {v2_name} : "))
        shape = function(v1, v2)
        print(f"The perimeter of {v1}cm for the {v1_name} and {v2}cm for the {v2_name} has {shape.getPerimeter()} cm")
        print(f"The area of {v1}cm for the {v1_name} and {v2}cm for the {v2_name} has  {shape.getArea()} cmˆ2")

    elif v3_name != None:
        v2 = int(input(f"Please input the value for {v2_name} : "))
        v3 = int(input(f"Please input the value for {v3_name} : "))
        shape = function(v1, v2, v3)
        print(f"The perimeter of {v1}cm for the {v1_name} and {v2}cm for the {v2_name} and {v3} for the {v3_name }has {shape.getPerimeter()} cm")
        print(f"The area of {v1}cm for the {v1_name} and {v2}cm for the {v2_name}  and {v3} for the {v3_name } has {shape.getArea()} cmˆ2")

    else:
        print(f"The perimeter of {v1}cm for the {v1_name} has {square.getPerimeter()} cm")
        print(
            f"The area f {v1}cm for the {v1_name} has  {square.getArea()} cmˆ2")


    rectangle = Rectangle(L, l)



if choose1 == '1':
    print("""Choose which shapes you want to work in :
    1) Rectangle
    2) Square
    3) Circle
    4) Equilateral Triangle
    """)
    choose2 = input("Please input your choose here : ")
    if choose2 == '1':
        print("\nWelcome to Rectangle Section Page!")
        print("You need two values to finish your work;")
        L = int(input("Please input the value for LENGTH : "))
        l = int(input("Please input the value for WIDTH : "))
        rectangle = Rectangle(L, l)
        print(f"The perimeter of {L}cm for the length and {l}cm for the width has {rectangle.getPerimeter()} cm")
        print(f"The area of {L}cm for the length and {l}cm for the width has  {rectangle.getArea()} cmˆ2")

    elif choose2 == '2':
        print("You need one values to finish your work :")
        s = int(input("Please input the value for side : "))
        square = Square(s)
        print(
            f"The perimeter of {s}cm for the side has {square.getPerimeter()} cm")
        print(
            f"The area of {s}cm for the side has  {square.getArea()} cmˆ2")

    elif choose2 == '3':
        print("You need two values to finish your work :")
        r = int(input("Please input the value for Radius : "))

        circle = Circle(r)
        print(
            f"The perimeter of {r}cm for the radius has {circle.getPerimeter()} cm")
        print(
            f"The area of {r}cm for the radius has {circle.getArea()} cmˆ2")

    elif choose2 == '4':
        print("You need one values to finish your work :")
        s = int(input("Please input the value for side : "))
        triangleE = Triangle(s)
        print(
            f"The perimeter of {s}cm for the side has {triangleE.getPerimeter()} cm")
        print(
            f"The area of {s}cm for the side has{triangleE.getArea()} cmˆ2")

    else:
        print("You've input some invalid character. Please try again.")

elif choose1 == 2:
    pass

else:
    print("Something wrong happening. Please try again!")
