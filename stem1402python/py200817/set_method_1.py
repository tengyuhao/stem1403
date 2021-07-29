"""
set method - copy
"""

set1 = {1, 2, 3}
set2 = set1.copy()
print(id(set1), id(set2))
print(set1 is set2)

set1 = {1, 2, 3}
set3 = set1
print(id(set1), id(set3))
print(set1 is set2)
770




