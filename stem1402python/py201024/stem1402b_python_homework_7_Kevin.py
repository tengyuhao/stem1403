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
num1 = input("Please input one number to be the dividend: ")
num2 = input("Please input one number to be the divisor: ")

try:
    num1 = int(num1)
except Exception as except_probl:
    print("This number \"{}\" is wrong, please try again.".format(num1))
    print(except_probl)
    while True:
        print()
        choix = input("Do you want to continue or quit. To continue, please type 1. To quit, please type 2: ")
        if choix == "1":
            while True:
                num1 = input("Please input one number to be the dividend: ")
                try:
                    num1 = int(num1)
                    break
                except Exception as except_probl3:
                    print(except_probl3)
        else:
            break

        break


try:
    num2 = int(num2)
except Exception as except_probl2:
    print("This \"{}\" is wrong, please try again.".format(num2))
    print(except_probl2)

    while True:
        print()
        choix2 = input("Do you want to continue or quit. To continue, please type 1. To quit, please type 2: ")
        if choix2 == "1":
            while True:
                num2 = input("Please input one number to be the divisor: ")
                try:
                    num2 = int(num2)
                    break
                except Exception as except_probl4:
                    print(except_probl4)
        else:
            break

        break

try:
    res = num1 / num2
    print(f"{num1} / {num2} = {res}")
except Exception as except_probleme2:
    print(except_probleme2)
    print("Good Bye! ")

print("====== End =======")



