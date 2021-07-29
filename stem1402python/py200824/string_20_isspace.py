"""
isspace()
returns True if there are only whitespace characters
in the string.
If not, it return False.
"""

# Example 1
s = '   \t'
print(s.isspace())

s = '   \n'
print(s.isspace())

s = ' a '
print(s.isspace())

s = ''
print(s.isspace())
