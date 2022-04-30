"""
bank interest query app
version: v1
"""


class Bank:
    def __init__(self, interestRate):
        self.interestRate = interestRate

    def getInterestRate(self):
        return self.interestRate


class BankA(Bank):
    def getInterestRate(self):
        return self.interestRate


class BankB(Bank):
    def getInterestRate(self):
        return self.interestRate


class BankC(Bank):
    def getInterestRate(self):
        return self.interestRate


class BankUtil:
    def queryInterestRate(self, bankObj):
        result = bankObj.getInterestRate()
        return result


# main
bank1 = BankA(0.04)
bank2 = BankB(0.0395)
bank3 = BankC(0.035)

myapp = BankUtil()
bank_dict = {'A': bank1, 'B': bank2, 'C': bank3}

var = input("Input the bank you want to check th interest : ")
"""
print("Query interest rate of BankA")
print(f'{myapp.queryInterestRate(bank1):.3%}')
print()

print("Query interest rate of BankB")
print(f'{myapp.queryInterestRate(bank2):.3%}')
print()

print("Query interest rate of BankC")
print(f'{myapp.queryInterestRate(bank3):.3%}')
"""

result = myapp.queryInterestRate(bank_dict[var])
print(f"{result:.3%}")


