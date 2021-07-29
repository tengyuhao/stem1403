"""
Number Formatting Types
Type Meaning
d Decimal integer
c Corresponding Unicode character
b Binary format
o Octal format
x Hexadecimal format (lower case)

n Same as 'd'. Except it uses current locale setting for number separator
e Exponential notation. (lowercase e)
f Displays fixed point number (Default: 6)
g General format. Rounds number to p significant digits. (Default precision: 6)
% Percentage. Multiples by 100 and puts % at the end.
"""

# d Decimal Integer
d = 12
print("Decimal Integer: {:6d}".format(d))

# c Corresponding Unicode character
c = 190
print("Corresponding Unicode character: {:c}".format(c))

# b Binary format
b = 35
print("Binary format: {:b}".format(b))

# o Octal format
o = 88
print("Octal format: {:o}".format(o))

# x Hexadecimal format
x = 160
print("Hexadecimal format: {:x}".format(x))

# n same as 'd'
n = 12
print("Decimal Integer: {:6n}".format(n))

# e  Exponential notation
e = 99
print("Exponential notation: {:.2e}".format(e))


# f Displays fixed point number
f = 76.77
print("Displays fixed point number: {:.2f}".format(f))

# g General format
g = 11.67
print("General format: {:.2g}".format(g))

# % Percentage
p = 0.90
print("Percentage: {:.0%}".format(p))
