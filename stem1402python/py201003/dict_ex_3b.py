"""
module 6.       datatype
chapter 6-6.    dictionary

Question:
Write a program to sort a dictionary by value
in both ascending and descending order.

Hints:
sorted()
module: lambda
dict()
"""

import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("Original dictionary :", d)

sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))
print("Dictionary in ascending order", sorted_d)


