"""
isnumeric()
returns True if all characters in a string are numeric characters.
If not, it returns False.
"""

# Example 1
s = '1242323'
print(s.isnumeric())

# s = '²3455'
s = '\u00B23455'
print(s.isnumeric())

# s = '½'
s = '\u00BD'
print(s.isnumeric())

s = '1242323'
s = 'python12'
print(s.isnumeric())
