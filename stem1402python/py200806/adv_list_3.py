"""
change value of items
"""

odd = [2, 4, 6, 8]

# change one item : 1st item
odd[0] = 1
odd[1] = 3
odd[2] = 5
odd[3] = 7
print(odd)

# change multiple items : 2nd item to the last
odd = [1, 4, 6, 8]
odd[1:4] = [3, 5, 7]
print(odd)

odd = [1, 4, 6, 8]
odd[1:4] = [3, 5, 7, 9]
print(odd)

odd = [1, 4, 6, 8]
odd[1:4] = [3, 5]
print(odd)

odd = [1, 4, 6, 8]
odd[1:4] = []
print(odd)
