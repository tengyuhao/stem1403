"""
2022.03.26
1. Programming practice
Write the program applying polymorphism
Problem: Bank Interest
Background:
Peter is living in a town. There are 3 banks in his town which are BankA, BankB, and BankC.
Each bank has a few branches.
He wants to know the interest rate of each bank, so that he could make a decision on which bank he is going to open a savings account at.
BankA - 0.04  (4%)
BankB - 0.0395 (3.95%)
BankC - 0.035 (3.5%)
Requirement:
Please write a small application for the residents of the town to easily check the current interest rate information of all banks at any time.
"""


class Bank:
    def __init__(self, name, rate):
        self.interest = rate
        self.name = name

    def check_interest(self):
        print(f"Interest of {self.name} is {self.interest} = {round(self.interest*100, 4)}%")


class BankA(Bank):
    pass


class BankB(Bank):
    pass


class BankC(Bank):
    pass


# main
bank_a1 = BankA('BankA', 0.04)
bank_b1 = BankB('BankB', 0.0395)
bank_c1 = BankC('BankC', 0.035)

print("Interest Check System")
print("If you want to check BankA, press A.")
print("If you want to check BankB, press B.")
print("If you want to check BankC, press C.")
res = input("Please put the value: ")
if res == "A":
    bank_a1.check_interest()

if res == "B":
    bank_b1.check_interest()

if res == "C":
    bank_c1.check_interest()
