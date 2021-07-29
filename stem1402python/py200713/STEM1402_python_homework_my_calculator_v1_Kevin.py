"""
my calculator
"""


def addition(x, y):
    summary = x + y
    return summary


def subtraction(x, y):
    difference = x - y
    return difference


def multiplication(x, y):
    product = x * y
    return product


def division(x, y):
    quotient = x / y
    return quotient


def operation_and(x, y):
    # if x == "True" and y == "True":
    #     return True
    # elif x == "True" and y == "False":
    #     return False
    # elif x == "False" and y == "True":
    #     return False
    # elif x == "False" and y == "False":
    #     return False
    # else:
    #     return "error"
    return x and y

def operation_or(x, y):
    if x == "True" and y == "True":
        return True
    elif x == "True" and y == "False":
        return True
    elif x == "False" and y == "True":
        return True
    elif x == "False" and y == "False":
        return False
    else:
        return "error"


def operation_not(x):
    if x == "True":
        return False
    elif x == "False":
        return True
    else:
        return "error"


# first line
print("====== Mini calculator ======")
print("Please choose the operation you want to choose: ")
print("1. addition \n2. subtraction \n3. multiplication \n4. division")
print("5. Logical operation(And, or, not)")

option_1 = float(input("Please enter the number of your choice: "))

if option_1 == 1:
    addend_1 = float(input("Please input the first addend: "))
    addend_2 = float(input("Please input the second addend: "))
    print(f"{addend_1} + {addend_2} = {addition(addend_1, addend_2)}")

elif option_1 == 2:
    minuend_1 = float(input("Please input the minuend: "))
    subtrahend_2 = float(input("Please input the subtrahend: "))
    print(f"{minuend_1} - {subtrahend_2} = {subtraction(minuend_1, subtrahend_2)}")

elif option_1 == 3:
    factor_1 = float(input("Please input the first factor: "))
    factor_2 = float(input("Please input the second factor: "))
    print(f"{factor_1} \u00D7 {factor_2} = {multiplication(factor_1, factor_2)}")

elif option_1 == 4:
    dividend = float(input("Please input the dividend: "))
    divisor = float(input("Please input the divisor: "))
    print(f"{dividend} \u00F7 {divisor} = {division(dividend, divisor)}")

elif option_1 == 5:
    print("1. And - 2. Or - 3. Not")
    option_2 = float(input("lease enter the number of your choice: "))
    x = input("Please input the first value boolean to do the logical operation. \n(True or False): ")
    if x == "True":
        x = True
    elif x == "False":
        x = False

    if option_2 == 1.0:
        y = input("Please input the second value boolean to do the logical operation. \n(True or False): ")
        print(f"{x} and {y} = {operation_and(x, y)}")

    elif option_2 == 2.0:
        y = input("Please input the second value boolean to do the logical operation. \n(True or False): ")
        print(f"{x} and {y} = {operation_or(x, y)}")

    elif option_2 == 3.0:
        print(f"not {x} = {operation_not(x)}")

    else:
        print("ERROR")

else:
    print("ERROR")




# eval()
