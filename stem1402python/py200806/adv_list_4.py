"""
add element
"""

odd = [2, 4, 6, 8]

# add one element at the tail
# append()
odd.append(10)
print(odd)
odd.append([11, 12])
print(odd)

# add multi-element at the tail
# extend
odd = [2, 4, 6, 8]
odd.extend([1, 3, 5])
print(odd)

