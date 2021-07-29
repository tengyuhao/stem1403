"""
d Decimal integer
c Corresponding Unicode character
b Binary format
o Octal format
x Hexadecimal format (lower case)
X Hexadecimal format (upper case)
n Same as 'd'. Except it uses current locale setting for number separator
e Exponential notation. (lowercase e)
E Exponential notation (uppercase E)
f Displays fixed point number (Default: 6)
F Same as 'f'. Except displays 'inf' as 'INF' and 'nan' as 'NAN'
g General format. Rounds number to
p significant digits. (Default precision: 6)
G Same as 'g'. Except switches to 'E' if the number is large.
% Percentage. Multiples by 100 and puts % at the end.
"""
saleoff = 0.5
print("This is product is on sale, {} off".format(saleoff))
print("This is product is on sale, {:.2%} off".format(saleoff))
print("This is product is on sale, {:.1%} off".format(saleoff))
print("This is product is on sale, {:.0%} off".format(saleoff))

