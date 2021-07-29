"""
isdigit()
returns True if all characters in a string are digits. If not, it returns False.

string.isdigit()
"""

# Example 1
s = "28112"
print(s.isdigit())


# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdigit())
print()
print()

# Example 2: String Containing digits and Numeric Characters
s = '23455'
print(s.isdigit())

#s = '²3455'
# subscript is a digit
s = '\u00B23455'
print(s.isdigit())

# s = '½'
# fraction is not a digit
s = '\u00BD'
print(s.isdigit())
