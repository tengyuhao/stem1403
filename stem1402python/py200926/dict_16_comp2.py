"""
1. Write a Python program to generate and print a dictionary that contains a number (between 1 and n)
in the form (x, x*x).
e.g. User inputs 5
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

n = 10
mydict = {key: key+key+1 for key in range(1, n+1)}

print(mydict)

# filter
mydict = {key: key+key+1 for key in range(1, n+1) if key % 2 == 1}
print(mydict)