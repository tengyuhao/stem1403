"""
set
A set is an unordered collection of items
unique items

set is mutable
items in set are immutable
"""

set1 = {1, 2, 3}
print(set1)

set1 = {1.1, 2.1, 3.1}
print(set1)

set1 = {'abc', 'abb', 'ccc'}
print(set1)

set1 = {(1, 2), 2, True}
print(set1)

# Error
# set1 = {[2, 3], [4, 5]}
# print(set1)

# set1 = {[2, 3], 'bac'''}
# print(set1)
