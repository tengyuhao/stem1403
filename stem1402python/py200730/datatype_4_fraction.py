"""
Python Fraction

Mathmatica
matlab

"""

import fractions
from fractions import Fraction as F
print(fractions.Fraction(0.5))

print(fractions.Fraction(1))

print(fractions.Fraction(1.5))

print(fractions.Fraction(1, 3))

print(fractions.Fraction(1.1))

print(2476979795053773/2251799813685248)

# 11/10
print(fractions.Fraction('1.1'))

print(fractions.Fraction('1.13'))


# 1/3 + 1/3 = 2/3
result = F(1, 3) + F(1, 3)
print(f"{F(1, 3)} + {F(1, 3)} = {result}")

result = F(1, 2) + F(1, 3)
print(f"{F(1, 2)} + {F(1, 3)} = {result}")

result = 1/F(1, 3)
print("1/F(1, 3) = {}".format(result))

result = 1/F(3, 1)
print("1/F(1, 3) = {}".format(result))

result = 1/F(5, 6)
print("1/F(1, 3) = {}".format(result))

result = F(-3, 10) > 0
print("1/F(1, 3) = {}".format(result))

