"""
[Homework]
1. Rewriting arithmetic calculator.
Accepting 2 inputs from a keyboard by users and output the division of these 2 values.
Requirements:
The 2 inputs should be converted to Integer before calculating.
Exception handling is required.
Your program should never crash in any case of input.
You may optimize your program.

"""
print("Welcome To My Mini Calculator")

def addition():
    print("======= addition part ==== ")
    num1 = input("Please input one number to be the first number in you addition: ")
    num2 = input("Please input one number to be the second number in your addition: ")
    try:
        num1 = float(num1)
        num2 = float(num2)
    except Exception as except_probleme:
        print(except_probleme)

    res = num1 + num2
    return res, "The number is not precis."


def division():
    print("======= Division part ========")
    num1 = input("Please input one number to be the dividend: ")
    num2 = input("Please input one number to be the divisor: ")

    try:
        num1 = int(num1)
        num2 = int(num2)
    except Exception as except_probleme:
        print(except_probleme)

    print(num1)
    print(num2)

    try:
        res = num1 / num2
        print(res)
    except Exception as except_probleme2:
        print(except_probleme2)

    print("====== End =======")
    return res

print(addition())







