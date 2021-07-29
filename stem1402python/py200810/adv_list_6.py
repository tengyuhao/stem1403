"""
insert items
"""

# case 1. insert a single item
# insert(index, item)
odd = [1, 9]
odd.insert(1, 3)
print(odd)

# case 2. insert multi item
odd[2:2] = [5, 7]
print(odd)

# odd[2:2] = []
# print(odd)