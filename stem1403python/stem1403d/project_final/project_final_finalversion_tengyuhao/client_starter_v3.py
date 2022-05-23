"""
Client Program - main program
Project : Plotter
Version Starter, 3.1
"""

from starter import *


def process_2d(name, value, v1_name, v2_name, v3_name, function):
    print(f"\nWelcome to {name} Section Page!")
    print(f"You need {value} values to finish your work;")
    v1 = float(input(f"Please input the value for {v1_name} : "))

    if v2_name is not None:

        v2 = float(input(f"Please input the value for {v2_name} : "))
        shape = function(v1, v2)
        print("Processing ...")
        print(f"The perimeter of {v1}cm for the {v1_name} and {v2}cm for the {v2_name} has {shape.getPerimeter()} cm.")
        print(f"The area of {v1}cm for the {v1_name} and {v2}cm for the {v2_name} has  {shape.getArea()} cmˆ2.")

    elif v3_name is not None:
        v2 = float(input(f"Please input the value for {v2_name} : "))
        v3 = float(input(f"Please input the value for {v3_name} : "))
        shape = function(v1, v2, v3)
        print("Processing ...")
        print(
            f"The perimeter of {v1}cm for the {v1_name} and {v2}cm for the {v2_name} and {v3} for the {v3_name}has {shape.getPerimeter()} cm.")
        print(
            f"The area of {v1}cm for the {v1_name} and {v2}cm for the {v2_name}  and {v3} for the {v3_name} has {shape.getArea()} cmˆ2.")

    else:
        shape = function(v1)
        print("Processing ...")
        print(f"The perimeter of {v1}cm for the {v1_name} has {shape.getPerimeter()} cm.")
        print(f"The area of {v1}cm for the {v1_name} has  {shape.getArea()} cmˆ2.")

    print(f"The {name} is drawing.")
    print(f"The {name} finished to draw.")


def process_3d(name, value, v1_name, v2_name, v3_name, function):
    print(f"\nWelcome to {name} Section Page!")
    print(f"You need {value} values to finish your work;")
    v1 = float(input(f"Please input the value for {v1_name} : "))

    if v2_name is not None:

        v2 = float(input(f"Please input the value for {v2_name} : "))
        shape = function(v1, v2)
        print("Processing ...")
        print(f"The volume of {v1}cm for the {v1_name} and {v2}cm for the {v2_name} has {shape.getVolume()} cmˆ3.")
        print(
            f"The surface area of {v1}cm for the {v1_name} and {v2}cm for the {v2_name} has  {shape.getSurfaceArea()} cmˆ2.")

    elif v3_name is not None:
        v2 = float(input(f"Please input the value for {v2_name} : "))
        v3 = float(input(f"Please input the value for {v3_name} : "))
        shape = function(v1, v2, v3)
        print("Processing ...")
        print(
            f"The volume of {v1}cm for the {v1_name} and {v2}cm for the {v2_name} and {v3} for the {v3_name}has {shape.getVolume()} cmˆ3.")
        print(
            f"The surface area of {v1}cm for the {v1_name} and {v2}cm for the {v2_name}  and {v3} for the {v3_name} has {shape.getSurfaceArea()} cmˆ2.")

    else:
        shape = function(v1)
        print("Processing ...")
        print(f"The volume of {v1}cm for the {v1_name} has {shape.getVolume()} cmˆ3.")
        print(f"The surface area f {v1}cm for the {v1_name} has  {shape.getSurfaceArea()} cmˆ2.")

    print(f"The {name} is drawing.")
    print(f"The {name} finished to draw.")


# main program
def main_section():
    print("\nWelcome to Project Potter. Choose that you want to work in 2D Shapes or 3D Shapes")
    print("* Please note some answers are maximum round in 14 figure after comma. All unites are in centimeters now.")

    print("1) 2D \n2) 3D\n3) Exit the system.")
    choose1 = input("Please input your choose here : ")
    return choose1


def principal_section(choose1):
    if choose1 == '1':
        print("""\nChoose which shapes you want to work in :
        1) Rectangle
        2) Square
        3) Circle
        4) Equilateral Triangle
        5) Exit the 2D Shapes section
        """)
        choose2 = input("Please input your choose here : ")
        if choose2 == '1':
            process_2d("Rectangle", 2, "LENGTH", "WIDTH", None, Rectangle)

        elif choose2 == '2':
            process_2d("Square", 1, "SIDE", None, None, Square)

        elif choose2 == '3':
            process_2d("Circle", 1, "RADIUS", None, None, Circle)

        elif choose2 == '4':
            process_2d("Equilateral Triangle", 1, "side", None, None, Triangle)

        elif choose2 == '5':
            pass

        else:
            print("You've input some invalid character. Please try again.")

        return choose2

    elif choose1 == '2':
        print("""\nChoose which shapes you want to work in :
            1) Sphere
            2) Cube
            3) Exit the 3D Shapes section
            """)
        choose2 = input("Please input your choose here : ")
        if choose2 == '1':
            process_3d("Sphere", 1, "RADIUS", None, None, Sphere)

        elif choose2 == '2':
            process_3d("Cube", 1, "SIDE", None, None, Cube)

        elif choose2 == "3":
            pass

        else:
            print("You've input some invalid character. Please try again.")

        return choose2
    elif choose1 == '3':
        pass

    else:
        print("Something wrong happening. Please try again!")


condition = False

while True:
    # main_section()
    if not condition:
        ch1 = main_section()
    if condition:
        pass

    # 2d section
    # print("Used") test data
    ch2 = principal_section(ch1)

    if ch1 == "1":
        if ch2 != "5":
            condition = True

        elif ch2 == "5":
            condition = False

    # 3d section
    elif ch1 == "2":
        if ch2 != "3":
            condition = True
        elif ch2 == "3":
            condition = False

    # to exit the program
    elif ch1 == "3":
        print("See you next time !")
        break

    else:
        condition = False
