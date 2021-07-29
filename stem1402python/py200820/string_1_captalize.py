"""
capitalize()

In Python, the capitalize() method converts first character
of a string to uppercase letter and lowercases all other characters, if any.

string.capitalize()
"""

# Example 1: Capitalize a Sentence

string = 'python is AWesone.'
print('Old String: ', string)

capitalized_string = string.capitalize()
print('Capitalized String:', capitalized_string)
print()

# Example 2: Non-alphabetic First Character
string = "* python is AWesome."
print('Old String: ', string)

capitalized_string = string.capitalize()
print('Capitalized String:', capitalized_string)