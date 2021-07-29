"""
casefold()

The casefold() method is an aggressive lower() method which converts
strings to case folded strings for caseless matching.

string.casefold()

lower()

"""

# Example 1
string = "PYTHON IS AWESOME"
new_string = string.casefold()
print("Lowercasser string:", new_string)
print()

# Example 2
firstString = "der Fluß"
secondString = "der Fluss"
if firstString.casefold() == secondString.casefold():
    print("They are equal.")
else:
    print("They are not equal.")

# Example 3
firstString = "Der Fluß"
print(firstString.lower())

# Example 4
firstString = "der"
print(firstString.upper())
